from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
    
@app.route('/naver')
def naver():
    return render_template('naver.html')

if __name__ == '__main__':
    app.run