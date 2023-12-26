from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<rota>')
def jessempadas(rota):
    if rota ==  'login':
        return render_template('loginU.html')
    elif rota == 'cadastro':
         return render_template('cadastroU.html')
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run()