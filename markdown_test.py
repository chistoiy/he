from markdown import markdown
from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_pagedown import  PageDown
from flask_pagedown.fields import PageDownField

 
from flask import request

app = Flask(__name__)
pagedown=PageDown()

app.config['WTF_CSRF_SECRET_KEY'] = 'IT 666 to 709 kill pic'
app.secret_key='123456'

class MyForm(FlaskForm):
	#name = StringField('name', validators=[DataRequired()])
	#pwd = StringField('pwd', validators=[DataRequired()])
	description = PageDownField('简介')
	submit=SubmitField('Submit')
#app.config['SECRET_KEY'] = 'you can't know'

@app.route('/',methods=['GET','POST'])
def login():
	if request.method=='POST':
		print(request.form['description'])
		return 'niha'
	form = MyForm()
	if form.validate_on_submit() :
		print(form.data())
		return 'OK'
	return render_template('markdown2.html',form=form)	
	
if __name__=='__main__':
	pagedown.__init__(app)
	app.run()