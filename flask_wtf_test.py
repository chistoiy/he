from flask import Flask,request,render_template,request


# from flask_wtf import FlaskForm,Form
# from wtforms import StringField
# from wtforms.validators import DataRequired
# class MyForm(FlaskForm):
#     name = StringField('name', validators=[DataRequired()])
#     pwd = StringField('pwd', validators=[DataRequired()])
#
# app = Flask(__name__)
# #app.config['SECRET_KEY'] = 'you can't know'
# app.config['WTF_CSRF_SECRET_KEY'] = 'IT 666 to 709 kill pic'
# app.secret_key='123456'
# @app.route('/',methods=['GET','POST'])
# def login():
# 	form = MyForm()
# 	if form.validate_on_submit() :
# 		return 'OK'
#
# 	return render_template('wtf.html',form=form)

#from flask_wtf import FlaskForm
from wtforms import StringField,Form
from wtforms.fields import simple
from wtforms import validators
class MyForm(Form):
	name = simple.StringField( )
	pwd = simple.StringField( )


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'you can't know'
app.config['WTF_CSRF_SECRET_KEY'] = 'IT 666 to 709 kill pic'
app.secret_key = '123456'


@app.route('/', methods=['GET', 'POST'])
def login():
	form = MyForm()
	if request.method=='POST':
		if form.validate():
			return 'OK'

	return render_template('wtf.html', form=form)



if __name__ =='__main__':
	app.run()
	
