'''
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello, world'

@app.route('/lock')
def disa():
    return 'hello, admin'

@app.route('/welcome')
def welcome():
    return render_template('flask_intro_html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
           error = 'Invealid credentials Pleas try again'
        else:
            return redirect(url_for('disa'))
    return render_template('flask_intro_html_2.html', error=error)


if __name__ == '__main__':
    app.run()
'''


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
flag = 0

def login_page(error):

    id = ['admin', 'haemin', 's_deo']
    password = ['3000', '1234', '0117']
    flag = 0

    for i in range(len(id)):
        if request.form['username'] == id[i] and request.form['password'] == password[i]:
            flag = 1

    if flag == 0:
        error = 'Invealid credentials Pleas try again'

    return flag, error



@app.route('/')
def home():
    return 'hello, world'

@app.route('/lock')
def disa():
    return 'hello, admin'

@app.route('/welcome')
def welcome():
    return render_template('flask_intro_html_2')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        flag,error = login_page(error)

    if flag == 1:
        return redirect(url_for('disa'))

    return render_template('flask_intro_html_2.html', error=error)


if __name__ == '__main__':
    app.run()