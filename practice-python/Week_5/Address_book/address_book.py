from flask import Flask, render_template, request
import sqlite3 as lite


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
	if request.method == 'POST':
		try:
			name = request.form['name']
			age = request.form['age']
			email = request.form['email']

			# 우리가 soup.find()를 한 것처럼 lite.connect를 한다. 안에 들어가는 인수는 우리가 사용할 db이다.
			# lite.connect는 : 내가 이 db를 플라스크에서 쓰겠다 라는 method임. 
			# with을 사용하게 되면 disconnect를 쓸 필요가 없어짐.
			with lite.connect('users.db') as conn:
				#실제로 커서를 만드는 행위이다
				cur = conn.cursor()
				# 커서를 이용해서 db를 실행하는 행위
				# sqlite 라이버리의 문법: ?, ?, ? 후 
				cur.execute("INSERT INTO user(name, age, email) VALUES(?, ?, ?)", (name, age, email))
				# 나 이제 이 행위 끝났어요 라고 해야 됨. 
				# commit을 적지 않으면 "비정상적인 접근"이라는 에러가 나오고 db를 들어갈 수 없게 됨. 그래서 다시 만들어야 됨. 
				conn.commit()
				msg = "signup complete"
		# 중간에 시행을 하다 혹시 무엇인가 잘못됬을 경우, db를 열기 전, 혹은 edit하기 전 상태로 가야된다.
		# 그러지 않으면 db가 잠기거나 문제가 생길 수 있다. 
		except:
			conn.rollback()
			msg = "signup failed"
		finally:
			# html다음 msg는 html안의 msg이다. html", msg = msg의 첫번째
			# 두번째는 현재 우리의 값이다.
			return render_template("signup.html", msg = msg)
			# 혹시나 db가 아직 닫혀있지 않을 것을 대비해 close를 해줘야 한다. 
			conn.close()

@app.route('/users')
def users():
	# db에서 정보를 갖고오자. 다시 연결을 한다
	conn = lite.connect("users.db")
	conn.row_factory = lite.Row

	cur = conn.cursor()
	cur.execute("SELECT * from user")

	rows = cur.fetchall()
	conn.close()

	# msg = msg를 했던 것처럼 html의 위치에 우리가 받아온 rows를 넣어주어야지 그려진다. 
	return render_template("users.html", rows = rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7070')