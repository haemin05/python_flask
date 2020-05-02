from flask import Flask

app = Flask(__name__)

@app.route('/haemin')
def helloworld():
    return 'hi'

@app.route('/')
def default_function():
    return 'default'

if __name__ == '__main__':
    app.run()

