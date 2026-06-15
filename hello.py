from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    """Index"""
    return "<h1>Hello, World!</h1>"

@app.route('/user/<name>')
def user(name):
    """User"""
    return f"<h1>Hello, {name}!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
