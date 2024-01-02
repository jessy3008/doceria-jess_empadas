from flask import Flask, render_template, request, url_for, redirect

import mysql.connector

app = Flask(__name__)

def conexaodb():
    conect = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='labinfo',
        database='jessempadas'
    )
    return conect


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('home.html')



@app.route('/loginU', methods=['POST'])
def loginU():
    return render_template('loginU.html')

@app.route('/carrinho', methods=['POST'])
def carrinho():
    return render_template('carrinho.html')

@app.route('/<rota>')
def jessempadas(rota):
    if rota ==  'login':
        return render_template('loginU.html')
    elif rota == 'cadastro':
         return render_template('cadastroU.html')
    else:
        return render_template('home.html')




@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "GET":
        return render_template('cadastroU.html')
    elif request.method == "POST":
        cpf = request.form.get('cpf')
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')
       
        
        connection = conexaodb()
        cursor = connection.cursor()
        
        cursor.execute('INSERT INTO usuario (cpf, nome, telefone, email, senha) VALUES (%s, %s, %s, %s, %s)', (cpf, nome, telefone, email, senha))
        connection.commit()
        
        
        cursor.close()
        connection.close()

        return redirect(url_for('home'))

    return render_template('cadastroU.html')


@app.route('/login', methods=['POST'])
def login():
    login_data = request.form.get('login')
    senha = request.form.get('senha')

    cadastra_se = request.form.get('cadastra')

    connection = conexaodb()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM usuario WHERE (cpf = %s OR email = %s) AND senha = %s', (login_data, login_data, senha))
    user = cursor.fetchone()

    if cadastra_se == True:
        return redirect(url_for('cadastro'))

    if user:
        cursor.close()
        connection.close()
        return redirect(url_for('home'))
    else:
        cursor.close()
        connection.close()
        return render_template('loginU.html', error_message="Credenciais inválidas. Tente novamente.")


if __name__ == '__main__':
    app.run(debug=True)

