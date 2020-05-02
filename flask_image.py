from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/img', methods=['POST'])
def img():

    temp = request.form['image_name']
    if request.method == 'POST':
        print(temp)
        return render_template('img_static.html', img=temp)

@app.route('/')
def helloworld():
    return render_template('button_edit.html')

if __name__ == '__main__':
    app.run()