from flask import Flask, render_template, request
import cv2
import os

app = Flask(__name__)


@app.route('/')
def picture_loader():
    return render_template('test.html')


@app.route('/cal', methods=['POST'])
def cal():
    path = request.form.get("path", 'not data')
    print("path", path)
    read = cv2.imread(path)

    cv2.imshow("test", read)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    app.run()