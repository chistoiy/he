from flask import Flask,render_template,request
import pymysql


app = Flask(__name__)

@app.route('/air/<pname>',methods=['GET','POST'])
def air(pname):
	conn=pymysql.Connection(host='localhost',port=3306,user='root',passwd='123456',db='s1125',charset='utf8')
	cursor = conn.cursor()
	if request.method=="POST":
		context = request.form.get('a')
		cursor.execute('select * from air_note where pname=%s',(pname))
		c = cursor.fetchone()
		if c:
			print('存在')
			cursor.execute('update air_note  set context = %s where pname=%s;',(context,pname))
			conn.commit()
			conn.close()
		else:
			cursor.execute('insert into air_note(pname,context) value(%s,%s);',(pname,context.encode('utf-8')))
			conn.commit()
			conn.close()
		if not context:
			print('delete everything')
			
		
		print(context)
		return '保存成功'
	
	
	cursor.execute('select * from air_note where pname=%s',(pname))
	data = cursor.fetchone()
	if not data:
		return render_template('air.html')
	#print(pname,data)
	return render_template('air.html',d=data[1])
	

if __name__=='__main__':
	app.run()