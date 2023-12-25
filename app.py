from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('loginU.html')

@app.route('/cadastro')
def home():
    return render_template('cadastroU.html')

if __name__ == "__main__":
    app.run()