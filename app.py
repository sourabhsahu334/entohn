from flask import Flask
from englisttohindi.englisttohindi import EngtoHindi

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/lang')
def chane_lang():
    message = "Yes, I am geeks"
    res = EngtoHindi(message)# put application's code here
    return res.convert



if __name__ == '__main__':
    app.run()
