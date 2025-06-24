from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def receive_data():
    username = request.form.get('username') 
    password = request.form.get('password')
    return f'Name: {username}, Password: {password}'   

if __name__ == "__main__":
    app.run(debug=True, host='192.168.18.34', port=5500)