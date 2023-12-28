'''from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)



@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/', methods=['GET', 'POST'])
cadastrdef o():
    if request.method == "GET":
        return render_template('cadastroU.html')
    elif request.method == "POST":
        cpf = request.form.get('cpf')
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')
        
        curso = mysql.connection.cursor()
        try:
            curso.execute('INSERT INTO usuario (cpf, nome, telefone, email, senha) VALUES (%s, %s, %s, %s, %s)', (cpf, nome, telefone, email, senha))
            mysql.connection.commit()
            curso.close()
        except Exception as e:
            print(f"Erro ao executar a query: {e}")

        curso.close()

        return redirect(url_for('home'))
    
    return render_template('cadastroU.html')



if __name__ == '__main__':
    app.run(debug=True)'''

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configurações do MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'jessempadas'
app.config['MYSQL_DB'] = 'labinfo'

# Inicialização do MySQL
mysql = MySQL(app)

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
        
        curso = mysql.connection.cursor()
        curso.execute('INSERT INTO usuario (cpf, nome, telefone, email, senha) VALUES (%s, %s, %s, %s, %s)', (cpf, nome, telefone, email, senha))
        mysql.connection.commit()
        curso.close()

        return redirect(url_for('home'))
    
    return render_template('cadastroU.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

