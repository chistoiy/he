from flask import Flask,request,render_template

app = Flask('__name__')

@app.route('/index')
def index():
	if request.method=='GET':
		return render_template('upload.html')
@app.route('/upload',methods=['GET','POST'])
def upload():
	if request.method=='POST':
		print('AAAAAAAAAAAAA')
		a = request.files['fil']
		print(type(a))
		return str(len(a.readlines()))
		#return a
if __name__=='__main__':
	app.run()