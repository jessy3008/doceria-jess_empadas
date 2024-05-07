from flask import Flask, render_template, request, url_for, redirect

import mysql.connector

app = Flask(__name__)

def conexaodb():
    conect = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='IFjenni23',
        database='jessempadas'
    )
    return conect


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('home'))
    
    connection = conexaodb()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT produto.nome, imagem.urlImagem
        FROM produto
        JOIN imagem ON produto.codproduto = imagem.codProduto
    """)
    produtos = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('home.html', produtos=produtos)

  


@app.route('/carrinho', methods=['POST'])
def carrinho():
    return render_template('carrinho.html')



@app.route('/loginU', methods=['POST']) #login usuario
def loginU():
    login_data = request.form.get('login')
    senha = request.form.get('senha')

    cadastra_se = request.form.get('cadastra')

    connection = conexaodb()
    cursor = connection.cursor()

    cursor.execute('SELECT senha FROM usuario WHERE cpf = %s OR email = %s', (login_data, login_data))
    user = cursor.fetchone()

    if cadastra_se == 'True':
        return redirect(url_for('cadastro'))

    elif user and senha(user[0], senha): 
        cursor.close()
        connection.close()
        return redirect(url_for('home'))
    else:
        cursor.close()
        connection.close()
        error = "Credenciais inválidas. Tente novamente."
        return render_template('loginU.html', error=error)





@app.route('/cadastro', methods=['GET', 'POST']) #cadastro usuario
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

        cursor.execute('INSERT INTO usuario (cpf, nome, telefone, email, senha) VALUES (%s, %s, %s, %s, %s)',
                       (cpf, nome, telefone, email, senha))
        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for('home'))

    return render_template('cadastroU.html')



@app.route('/login', methods=['POST'])    # login
def login():
    login_data = request.form.get('login')
    senha = request.form.get('senha')

    cadastra_se = request.form.get('cadastra')

    connection = conexaodb()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM usuario WHERE (cpf = %s OR email = %s) AND senha = %s', (login_data, login_data, senha))
    user = cursor.fetchone()

    if cadastra_se == 'True':  
        return redirect(url_for('cadastro'))

    elif user:
        cursor.close()
        connection.close()
        return redirect(url_for('home'))
    else:
        cursor.close()
        connection.close()
        error = "Credenciais inválidas. Tente novamente."
        return render_template('loginU.html', error=error)



@app.route('/adm_cadastra', methods=['GET', 'POST']) #cadastro de adm
def adm_cadastra():
    if request.method == "GET":
        return render_template('adm.html')
    elif request.method == "POST":
        cnpj = request.form.get('cnpj')
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        telefone = request.form.get('telefone')
       
        
        connection = conexaodb()
        cursor = connection.cursor()
        
        cursor.execute('INSERT INTO fornecedor (cnpj, nome, telefone, email, senha) VALUES (%s, %s, %s, %s, %s)', (cnpj, nome, telefone, email, senha))
        connection.commit()
        
        
        cursor.close()
        connection.close()

        return redirect(url_for('cadastrarP')) 

    return render_template('adm.html')

@app.route('/adm', methods=['POST','GET']) #login de adm
def adm():
    login_data = request.form.get('login')
    senha = request.form.get('senha')

    cadastra_se = request.form.get('cadastra')

    connection = conexaodb()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM fornecedor WHERE (cnpj = %s OR email = %s) AND senha = %s', (login_data, login_data, senha))
    user = cursor.fetchone()

    if cadastra_se == 'True':  
        return redirect(url_for('cadastrarP'))  

    if user:
        cursor.close()
        connection.close()
        return redirect(url_for('cadastrarP'))  
    else:
        cursor.close()
        connection.close()
        return render_template('loginADM.html', error_message="Credenciais inválidas. Tente novamente.")

@app.route('/cadastrarP', methods=['GET', 'POST']) #cadastro de produto
def cadastrarP():
    if request.method == "GET":
        return render_template('cadastrarP.html')
    elif request.method == "POST":
        cnpj = request.form.get('cnpj')
        categoria = request.form.get('categoria')
        nome = request.form.get('nome')
        codproduto = request.form.get('codproduto')
        descricao = request.form.get('descricao')
        lote = request.form.get('lote')
        vencimento = request.form.get('vencimento')
        quantidade = request.form.get('quantidade')
        valor = request.form.get('valor')
        img = request.files['img']

        extensao = img.filename.rsplit('.',1)[1]

        url = f'static/img/{codproduto}.{extensao}'

        img.save(url)
            

        connection = conexaodb()
        cursor = connection.cursor()

        cursor.execute('INSERT INTO produto (codproduto, lote, vencimento, quantidade, valor, nomeCategoria, descricao, nome, cnpjFornecedor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (codproduto, lote, vencimento, quantidade, valor, categoria, descricao, nome, cnpj))
        connection.commit()

        cursor.execute('INSERT INTO imagem (codProduto, urlImagem) VALUES (%s, %s)', (codproduto, url))
        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for('home'))

    return render_template('cadastrarP.html')


    


if __name__ == '__main__':
    app.run(debug=True)

