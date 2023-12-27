#pip install Flask-MySQLdb

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configurações do banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'labinfo'
app.config['MYSQL_DB'] = 'jessempadas'

# Inicialização do MySQL
mysql = MySQL(app)

@app.route('/', methods=['POST'])
def cadrasto():
    if request.method == "GET":
        return render_template('cadastroU.html')
    elif request.method == "POST":
        cpf = request.form.get('cpf')
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')
        print(request.get)
        cursor = mysql.connection.cursor()

        cursor.execute('INSERT INTO usuarios (cpf, nome, telefone, email, senha) VALUES (%s, %s, %s, %s, %s)', (cpf, nome, telefone, email, senha))

        return redirect(url_for('home'))
    
    return render_template('cadastroU.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)