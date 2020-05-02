from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template('flask_intro_html_1',None)

@app.route('/haemin', methods=['POST'])
def cal():
    temp = request.form['hello']
    if temp == 'hello':
        return 'bye'
    else:
        return 'nice to meet you'

if __name__ == '__main__':
    app.run()