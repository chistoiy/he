from flask import Flask,request,render_template
from utils.bdy import a as bd

app = Flask(__name__)

@app.route('/bdy',methods=['POST','GET'])
def bdy():
	if request.method == 'GET':
		return render_template('bdy.html')
	select_key = request.form.get('select_key')
	k = bd(select_key).values()
	#print(k,type(k))
	return render_template('bdy_show.html',j = list(k))
	

if __name__=='__main__':
	app.run()