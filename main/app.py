from flask import Flask, render_template, request, url_for, redirect

import mysql.connector

app = Flask(__name__)

def conexaodb():
    conect = mysql.connector.connect(
    MYSQL_HOST = '127.0.0.1',
    MYSQL_USER = 'root',
    MYSQL_PASSWORD = 'labinfo',
    MYSQL_DB = 'jessempadas')

    return conect

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == "GET":
        return render_template('cadastroU.html')
    elif request.method == "POST":
        cpf = request.form.get('cpf')
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')

        # Call the conexaodb function to get the connection
        connection = conexaodb()
        cursor = connection.cursor()

        cursor.execute('INSERT INTO usuario (cpf, nome, telefone, email, senha) VALUES (%s, %s, %s, %s, %s)', (cpf, nome, telefone, email, senha))
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return redirect(url_for('home'))
    
    return render_template('cadastroU.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()


'''@app.route('/')
def home():

    return render_template('home.html')

@app.route('/<rota>')
def jessempadas(rota):
    if rota ==  'login':
        return render_template('loginU.html')
    elif rota == 'cadastro':
         return render_template('cadastroU.html')
    else:
        return render_template('home.html')'''
