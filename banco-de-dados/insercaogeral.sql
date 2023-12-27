use jessempadas;

-- Inserção tabela `usuario`
INSERT INTO usuario (cpf, nome, email, senha, telefone, urlImagem)
VALUES ('222.222.222-22', 'Jose', 'jose@email.com', 'senha456', '987654321', NULL);

-- Inserção de dados na tabela `compra`
INSERT INTO compra (valor, cpfUsuario, datacompra, quantidade)
VALUES (2.50, '222.222.222-22', '2023-12-31', 1);


-- Inserção de dados na tabela `carrinho`
INSERT INTO carrinho (cpfUsuario, codProduto, quantidade, codCompra)
VALUES ('222.222.222-22', 9, 1, 1);


-- Inserção de dados na tabela `enderecoUsuario`
INSERT INTO enderecoUsuario (cpfUsuario, rua, numero, bairro, cidade, estado, pais)
VALUES ('222.222.222-22', 'Rua General Avelino', 123, 'Bairro Petrolina', 'Bom Jesus', 'AC', 'Brasil');

-- Inserção de dados na tabela `enderecoFornecedor`
INSERT INTO enderecoFornecedor (cnpjFornecedor, rua, numero, bairro, cidade, estado, pais)
VALUES ('11.111.111/0001-11', 'Rua Batista Almeida', 456, 'Bairro Longa Vista', 'Goianinha', 'RN', 'Brasil');
