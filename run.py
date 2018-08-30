from flask import Flask, render_template, request
import sqlite3 as sql
from random import choice
email=0

app = Flask(__name__)

		
#flask

@app.route("/")
def hello_user():
    return render_template('login.html')

@app.route("/log")
def log():
    return render_template('login.html')



@app.route("/chatHome")
def chatHome():
	if email==0:
		return render_template('login.html')
	else:
		return render_template('chatHome.html')
	
@app.route("/chat1")
def chat1():
	if email==0:
		return render_template('login.html')
	else:
		return render_template('chat1.html')

	
@app.route("/chat11",methods=['post'])
def chat11():
	if email==0:
		return render_template('login.html')
	else:
		conn=sql.connect('mydatabase.db')
		cur=conn.cursor()
		source=request.form['source'].upper()
		print(source)
		destin=request.form['destination'].upper()
		print(destin)
		cur.execute("SELECT * FROM flight where dst=\""+destin+"\" and src=\""+source+"\"")
		row=cur.fetchall()
		conn.close()
		print(row)
		return render_template('chat1.html',row=row)
		
	
	
@app.route("/chat41",methods=['post'])
def chat41():
	if email==0:
		return render_template('login.html')
	else:
		conn=sql.connect('mydatabase.db')
		cur=conn.cursor()
		source=request.form['src'].upper()
		print(source)
		destin=request.form['dst'].upper()
		print(destin)
		cur.execute("SELECT f_code,f_name,src,dst,jny_time FROM flight where dst=\""+destin+"\" and src=\""+source+"\"")
		row=cur.fetchall()
		conn.close()
		print(row)
		return render_template('chat4.html',row=row)
	
		


	
@app.route("/chat42",methods=['post'])
def chat42():
	global email
	if email==0:
		return render_template('login.html')
	else:
		conn=sql.connect('mydatabase.db')
		cur=conn.cursor()
		num=650
		code=request.form['code'].upper()
		print(code)
		cur.execute("SELECT * FROM flight where f_code=\""+code+"\"")
		res=cur.fetchall()
		print(res)
		cur.execute("SELECT pnr_id FROM passenger where email=\""+email+"\"")
		row=cur.fetchall()
		print(row)
		cur.execute("SELECT count(*) FROM reservation")
		tkid=cur.fetchone()
		num=num+tkid[0]
		print(num)
		a=row[0][0]
		b=res[0][0]
		c=res[0][4]
		d=res[0][5]
		e=res[0][2]
		f=res[0][3]
		print(a)
		print(b)
		print(c)
		print(d)
		print(e)
		print(f)
		date=c.split('-')
		req=[date[2],date[1],date[0]]
		result='-'.join(req)
		print(result)
		cur.execute("insert into reservation values ("+str(a)+",\"AB"+str(num)+"\",\""+b+"\",\""+date[2]+"-"+date[1]+"-"+date[0]+"\",\""+d+"\",\""+e+"\",\""+f+"\")")
		conn.commit();
		cur.execute("UPDATE `reservation` SET `jny_date`="+str(res[0][4])+" WHERE pnr_id="+str(a)+"")
		conn.commit();
		conn.close()
		return render_template('chat4.html')
	
		
	
	
@app.route("/chat21",methods=['post'])
def chat21():
	if email!=0:
		return render_template('login.html')
	else:
		conn=sql.connect('mydatabase.db')
		cur=conn.cursor()
		flightid=request.form['flightid'].upper()
		print(flightid)
		cur.execute("SELECT * FROM flight where f_code=\""+flightid+"\"")
		row=cur.fetchall()
		conn.close()
		print(row)
		return render_template('chat2.html',row=row)
	
		
	
	
@app.route("/chat31",methods=['post'])
def chat31():
	if email!=0:
		return render_template('login.html')
	else:
		conn=sql.connect('mydatabase.db')
		cur=conn.cursor()
		passenger=request.form['flight'].upper()
		print(passenger)
		cur.execute("SELECT * FROM reservation where pnr_id=\""+passenger+"\"")
		row=cur.fetchall()
		print(row)
		cur.execute("SELECT * FROM payment where pnr_id=\""+passenger+"\"")
		pay=cur.fetchall()
		print(pay)
		conn.close()
		return render_template('chat3.html',pay=pay,row=row)	
	
		
	
@app.route("/chat2")
def chat2():
	if email==0:
		return render_template('login.html')
	else:
		return render_template('chat2.html')
	
	
@app.route("/chat3")
def chat3():
	if email==0:
		return render_template('login.html')
	else:
		return render_template('chat3.html')
	
	
@app.route("/chat4")
def chat4():
	if email==0:
		return render_template('login.html')
	else:
		return render_template('chat4.html')
	
# signing up
@app.route("/signup",methods=['POST'])
def signup():
	global email
	conn=sql.connect('mydatabase.db')
	cur=conn.cursor()
	fname=request.form['f_name'].upper()
	print(fname)
	lname=request.form['l_name'].upper()
	print(lname)
	countrey=request.form['countrey'].upper()
	print(countrey)
	gender=request.form['group1'].upper()
	print(gender)
	dob=request.form['dob'].upper()
	print(dob)
	address=request.form['address'].upper()
	print(address)
	email=request.form['email'].lower()
	print(email)
	password=request.form['password'].lower()
	print(password)
	phone=request.form['phone'].upper()
	print(phone)
	passport=request.form['idc'].upper()
	print(passport)
	cur.execute("select pnr_id from passenger")
	idch=cur.fetchall()
	pnr=(choice([i for i in range(0,999) if i not in idch]))
	cur.execute("insert into  passenger (pnr_id,address,nationality,name,gender,ph_no,passport,email,password,dob,lastname) values("+str(pnr)+",\""+address+"\",\""+countrey+"\",\""+fname+"\",\""+gender+"\","+phone+",\""+passport+"\",\""+email+"\",\""+password+"\","+str(dob)+",\""+lname+"\")")
	conn.commit();
	conn.close()
	return render_template('chatHome.html')

#logging in
@app.route("/login",methods=['POST'])
def login():
	conn=sql.connect('mydatabase.db')
	cur=conn.cursor()
	global email
	email=request.form['email'].lower()
	print(email)
	password=request.form['password'].lower()
	print(password)
	try:
		cur.execute("SELECT email,password FROM passenger where email=\""+email+"\"")
		det=cur.fetchall()
	except:
		error=1
		return render_template('login.html',error=error)
	if email==det[0][0] and password==det[0][1]:
		return render_template('chatHome.html')
	else:
		error=1
		return render_template('login.html',error=error)


if __name__ == "__main__":
    app.run(debug=True)

