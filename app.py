from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('apple.html')

if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
