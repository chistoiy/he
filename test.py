from flask import Flask,url_for,jsonify,make_response
app = Flask(__name__,template_folder='templates',static_folder='static')


#从文件内导入设置信息
#路由，json，自定义报头

@app.route('/',)#endpoint='root_path' 路由命名，用于给url_for进行反向生成url
def root():
	print('nihao')
	#print(url_for('root_path'))
	return '你好'
	
@app.route('/path/<niha>')#动态路由
def path(niha):
	
	return niha
@app.route('/ways/<int:nihao>')#动态路由
def ways(nihao):
	print(url_for('ways',nihao=213))
	return 'kk{}'.format(nihao)

@app.route('/json_test')
def json_test():
	dic = {'a':'aa','b':'bb'}
	return jsonify(dic)

@app.route('/head')
def head():
	dic = {'a':'aa','b':'bb'}
	obj = make_response(jsonify(dic))
	obj.headers['xxxx']='123'
	
	return obj
	
	
if __name__=='__main__':
	app.config.from_object('settings.DevelopmentConfig')
	app.run(port=1234)
	
import importlib

#setting文件内设置一个Foo类，然后这个类的属性设置了app的属性
