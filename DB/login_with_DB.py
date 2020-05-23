from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)

app.secret_key = b'1234abc'

con = sqlite3.connect("join_info.db")
cur = con.cursor()
try:
    cur.execute("CREATE TABLE haemin(id text PRIMARY KEY , PW text)")
    con.commit()
    con.close()

except:
    print('already DB')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if not session.get('logged_in'):
        if request.method == 'POST':
            con = sqlite3.connect('join_info.db')
            cur = con.cursor()
            login_id = request.form.get('id', "not data")
            login_pwd = request.form.get('pwd', "not data")

            if login_id == "not data":
                return render_template('login.html')

            execute = 'SELECT * FROM haemin where id =(?)'
            cur.execute(execute, login_id)
            rows = cur.fetchall()
            con.commit()
            con.close()

            try:
                if rows[0][1] == login_pwd:
                    print('Sucees login')
                    session['logged_in'] = True
                    return redirect(url_for('welcome'))

            except:
                print('Fail login')
                return render_template('login.html')
    else:
        return redirect(url_for('welcome'))

    return render_template('login.html', error=error)

@app.route('/sing_up/', methods=['POST'])
def sing_up():
    if request.method == 'POST':
        con = sqlite3.connect('join_info.db')
        cur = con.cursor()

        want_id = request.form.get('want_id', "not data")
        want_pwd = request.form.get('want_pwd', "not data")

        if want_id == "not data":
            return render_template('join.html')


        try:
            execute = "INSERT INTO haemin(ID, PW)VALUES(?,?)"
            cur.execute(execute, (want_id, want_pwd))
            print('Success Join')
            con.commit()
            con.close()
            return redirect(url_for('login'))
        except:
            print('Fail Join')
            return render_template('join.html')

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/logout')
def logoutt():
    session.pop('logged_in', None)
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run()