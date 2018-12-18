from flask import Flask,url_for,render_template,redirect,abort
app = Flask(__name__)

#@app.route('/')
#def hello_world():

#	return '这是根目录'

@app.route('/projects/')
def projects():
    return 'The project page'



	

@app.route('/path/<subpath>')
def a(subpath):
	return subpath+'这是带子路径的显示'	
@app.route('/index', methods=['GET','POST'])
def index():
	#return render_template('404.html',)
	abort(404)
    #this_is_never_executed()
	page_not_found()
    #return 'index'
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404	

@app.route('/login')
def login():
	return redirect(url_for('index')) #使用重定向加url_for路由反向解析
    #return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
	
if __name__ == '__main__':
    app.run(debug=True)