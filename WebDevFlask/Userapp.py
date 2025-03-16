from flask import Flask

def make_bold(fun):
    def wrapper():
        return '<b>' + fun() + '</b>'
    return wrapper   

def make_emphasis(fun):
    def wrapper():
        return f'<em>{fun()}<em>' 
    return wrapper

def underline(fun):
    def wrapper():
        return f'<u>{fun()}</u>'
    return wrapper

app = Flask(__name__)

@app.route('/username/<name>')
def greetings(name):
    return f'<h1>Hello, {name}</h1>'

@app.route('/bye')
@make_bold
@make_emphasis
@underline
def bye():
    return 'Bye'

if __name__ == '__main__':
    app.run(debug=True)