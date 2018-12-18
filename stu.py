from flask import Flask,render_template,redirect,url_for,session,request,Markup,flash，get_flashed_messages
import functools
app = Flask(__name__)
app.config.from_object('settings.DevelopmentConfig')

#装饰器检测登陆校验
#使用before_request()来批量校验

STUDENT_DICT={
	1:{'name':'小王','age':12,'gender':'male'},
	2:{'name':'小东北','age':22,'gender':'male'},
	3:{'name':'小田','age':21,'gender':'female'},
	}
	
#检测是否登陆的装饰器，一般只用于少数页面
def auth(func):
	@functools.wraps(func)
	def inner(*args,**kwargs):
		if not session.get('user'):
			return redirect(url_for('login'))
		ret = func(*args,**kwargs)
		return ret
	return inner
	
	
#用于全局检测登陆，函数名自定义，函数内容为其他方法被请求响应前执行
#同时其他视图函数前不需要修改装饰器
#@app.before_request
#def xxxx():
	#if request.path =='/login':
	#	return None
	#if session.get('user'):
	#	return None
	#return redirect(url_for('login'))
	
@app.route('/index')
@auth
def index():
	return render_template('index.html',stu_dic=STUDENT_DICT,session=session)
	
@app.route('/delete/<int:nid>')
@auth
def delete(nid):
	if nid in STUDENT_DICT.keys():
		STUDENT_DICT.pop(nid)
	return redirect(url_for('index'))
	
@app.route('/detail/<int:nid>')
@auth
def detail(nid):
	if nid in STUDENT_DICT.keys():
		info = STUDENT_DICT[nid]	
	return render_template('detail.html',info=info)

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('login.html',error='')
	user = request.form.get('user')
	print(user)
	pwd = request.form.get('pwd')
	print(pwd)
	if user == 'qwe' and pwd == '123':
		session['user']= user
##session在被使用时需要配置SECRET_KEY的值，即对session进行加盐加密
##过程时，flask读取浏览器的cookie中的session对应的值，然后将之解密并反序列化后形成字典，载入内存
		return redirect('/index')
	return render_template('login.html',error='用户名错误')
@app.route('/logout',methods=['GET'])
def logout():
	session.pop('user')
	return redirect('/login')

	

########模板	
##与django使用模板一样
##模板内设置这个可以重复显示,宏定义，定义一个函数
"""
{% macro ccc(name,type='text',value='') %}
			<h1>宏</h1>
			<input type='text'>
	
	{% endmacro %}
	
	{{ ccc(1) }}
	{{ ccc(1) }}
"""
@app.template_global()#设置一个全局的方法，变量，在模板读取时，render_template不需要写该方法名即可传递
def b(b1):
	return b1+1

@app.template_filter()#与global区别在于，主要针对这样的使用形式，{{1|c(2,3)}}，即存在管道符
def c(c1,c2,c3):
	return c1+c2+c3

@app.route('/tpl')
def tpl():
	context = {
		'users':['xs','xl','xz'],
		'a':Markup("<input type='text'/>")
	}
	return render_template('tpl.html',**context)
	
	
#####闪现
"""
flash('临时数据存储')
相当于存储一个参数在session里，但是只能取一次，之后就会被删除，等于取完后从session内pop掉
print(get_flashed_messages())

把这些数据按类别存储和取
flash('临时数据存储','error')
get_flashed_messages(category_filter=['error'])

"""
@app.route('/page1')
def page1():
	#session['uuuu'] = 123
	flash('临时数据存储')
	return 'session1'
@app.route('/page2')
def page2():
	#print(session['uuuu'])
	#session.pop('uuuu')
	print(get_flashed_messages())
	return 'session2'

	
######z中间件
class MiddleWare:
    def __init__(self,wsgi_app):
        self.wsgi_app = wsgi_app
  
    def __call__(self, *args, **kwargs):
		
        ret = self.wsgi_app(*args, **kwargs)
		return ret
if __name__=='__main__':
	app.wsgi_app = MiddleWare(app.wsgi_app)
	app.run()