CREATE SCHEMA TRB02;

CREATE TABLE TRB02.tb_categorias (
	id_categoria INTEGER,
    titulocategoria VARCHAR(40),
    descricaocategoria VARCHAR(100),
    fg_ativo INTEGER,
    CONSTRAINT pk_tb_categorias_idcategoria PRIMARY KEY (id_categoria)
    
);

CREATE TABLE TRB02.tb_fornecedores (
	id_fornecedor INTEGER,
    cnpj VARCHAR(20),
    razaosocial VARCHAR(50),
    telefone  VARCHAR(12),
    endereco VARCHAR(60),
    contato VARCHAR(30),
    fg_ativo INTEGER,
    CONSTRAINT pk_tb_fornecedores_idfornecedores PRIMARY KEY (id_fornecedor)
    
);

CREATE TABLE TRB02.tb_produtos (
    id_produtos INTEGER,
    id_fornecedor INTEGER,
    id_categoria INTEGER,
    nomeproduto VARCHAR(40),
    descricaoproduto VARCHAR(100),
    valorunitario NUMERIC(1),
    quantidade INTEGER,
    quantidademinima INTEGER,
    fg_ativo INTEGER,
    CONSTRAINT pk_tb_produtos_idprodutos PRIMARY KEY (id_produtos),
    CONSTRAINT fk_tb_produtos_idfornecedor FOREIGN KEY (id_fornecedor) REFERENCES TRB02.tb_fornecedores (id_fornecedor),
    CONSTRAINT fk_tb_produtos_idcategoria FOREIGN KEY (id_categoria) REFERENCES TRB02.tb_categorias (id_categoria)
    );
    
CREATE TABLE TRB02.tb_vendedores(
    id_vendedor INTEGER,
    cpf VARCHAR(14),
    nome VARCHAR(40),
    carteiradetrabalho VARCHAR(5),
    telefone VARCHAR(12),
    dataadmissao DATE,
    fg_ativo INTEGER,
    CONSTRAINT pk_tb_vendedores_idvendedor PRIMARY KEY (id_vendedor)
    );
    
CREATE TABLE TRB02.tb_compras (
    id_compra INTEGER,
    id_fornecedor INTEGER,
    id_produtos INTEGER,
    id_categoria INTEGER,
    datacompra DATE,
    valortotal NUMERIC(15,2),
    quantidade INTEGER,
    fg_ativo INTEGER,
    CONSTRAINT pk_tb_compras_idcompra PRIMARY KEY (id_compra),
    CONSTRAINT fk_tb_compras_idprodutos FOREIGN KEY (id_produtos) REFERENCES TRB02.tb_produtos (id_produtos),
    CONSTRAINT fk_tb_compras_idfornecedor FOREIGN KEY (id_fornecedor) REFERENCES TRB02.tb_fornecedores (id_fornecedor),
    CONSTRAINT fk_tb_compras_idcategoria FOREIGN KEY (id_categoria) REFERENCES TRB02.tb_categorias (id_categoria)
    );
    
 CREATE TABLE TRB02.tb_vendas (
    id_venda INTEGER,
    id_vendedor INTEGER,
    id_categoria INTEGER,
    id_produtos INTEGER,
    datavenda DATE,
    valortotal NUMERIC(15,2),
    quantidade INTEGER,
    fg_ativo INTEGER,
    CONSTRAINT pk_tb_vendas_idvenda PRIMARY KEY (id_venda),
    CONSTRAINT fk_tb_vendas_idprodutos FOREIGN KEY (id_produtos) REFERENCES TRB02.tb_produtos (id_produtos),
    CONSTRAINT fk_tb_vendas_idvendedor FOREIGN KEY (id_vendedor) REFERENCES TRB02.tb_vendedores (id_vendedor),
    CONSTRAINT fk_tb_vendas_idcategoria FOREIGN KEY (id_categoria) REFERENCES TRB02.tb_categorias (id_categoria)
    );

