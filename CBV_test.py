from flask import Flask,views,url_for
from werkzeug.routing import BaseConverter
"""
	CBV形式
		methods
		装饰器
	自定义正则
	
"""


app = Flask(__name__)


	
class UserView(views.MethodView):
	methods = ['GET','POST']
	#装饰器函数与FBV一样，但使用时直接填写到decorators内，get和post在执行时自动执行装饰器内容
	decorators = []

	def get(self,*args,**kwargs):
		return 'GET'
	def post(self,*args,**kwargs):
		return 'POST'	
app.add_url_rule('/user',None,UserView.as_view('uuuu'))


#正则
"""
路由传递匹配成功后将结果传送给to_python，然后将结果返回给视图函数
"""
class RegexConverter(BaseConverter):
	def __init__(self,map,regex):
		super(RegexConverter,self).__init__(map)
		self.regex = regex
	def to_python(self,value):
		return int(value)
	def to_url(self,value):
	#在反向解析url时使用
		val = super(RegexConverter,self).to_url(value)
		return val
app.url_map.converters['reg'] = RegexConverter

@app.route('/index/<reg("\d+"):nid>')
def index(nid):
	print(url_for('index',nid=987))
	return 'index'+str(nid)

if __name__ == "__main__":
	app.run(port=1234)