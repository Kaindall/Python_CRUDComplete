DB_NAME = "eshop"

TABLES = {}
TABLES["client"] = ("""
    CREATE TABLE IF NOT EXISTS client (
	idClient INT AUTO_INCREMENT PRIMARY KEY,
    Cname VARCHAR(15),
    Csurname VARCHAR (45),
    cpf CHAR(11) NOT NULL,
    phone INT,
    email VARCHAR(70) NOT NULL,
    birthdate DATE,
    street VARCHAR (70),
    s_number INT,
    city VARCHAR(45),
    state VARCHAR(45),
    CONSTRAINT client_cpf UNIQUE (cpf)
) ENGINE=InnoDB""")

TABLES["product"] = ("""
    CREATE TABLE IF NOT EXISTS product (
	idProduct INT AUTO_INCREMENT PRIMARY KEY,
    Pname VARCHAR(45),
    category ENUM("Toy", "Mechanic", "Domestic", "Eletronic", "Clothing", "Food"),
    price FLOAT NOT NULL,
    underage BOOLEAN DEFAULT false,
    rating FLOAT DEFAULT 0
) ENGINE=InnoDB""")

TABLES["payment"] = ("""
    CREATE TABLE IF NOT EXISTS payment (
	idPayment INT AUTO_INCREMENT,
    idClient INT,
    paymentType ENUM ("QR Code", "Pix", "Credit Card", "Debit Card", "Two Cards"),
    verification_code VARCHAR(20),
    validity DATE,
    value_limit FLOAT,
    useful BOOL DEFAULT false,
    PRIMARY KEY (idPayment, idClient),
    CONSTRAINT fk_payment_client FOREIGN KEY (idClient) REFERENCES client (idClient) ON UPDATE CASCADE
) ENGINE=InnoDB""")

TABLES["request"] = ("""
    CREATE TABLE IF NOT EXISTS request (
	idOrder INT AUTO_INCREMENT,
    idClient INT,
    idPayment INT,
    statement ENUM ("Waiting Payment", "Paid", "Travelling", "Finished", "Canceled") DEFAULT "Waiting Payment",
    details VARCHAR (255),
    price FLOAT NOT NULL,
    PRIMARY KEY (idOrder, idClient),
    CONSTRAINT fk_orders_payment FOREIGN KEY (idPayment, idClient) REFERENCES payment(idPayment, idClient) ON UPDATE CASCADE
) ENGINE = InnoDB""")

TABLES["delivery"] = ("""
    CREATE TABLE IF NOT EXISTS delivery (
	idDelivery INT AUTO_INCREMENT,
    idOrder INT,
	delivery_cost FLOAT DEFAULT 0,
    delivery_status ENUM ("Waiting Confirmation", "Unpacking", "Detaching", "Sending to the Carrying", "In Travel", "Delivered") 
    DEFAULT "Waiting Confirmation",
    sender_adress VARCHAR (255),
    final_adress VARCHAR (255),
    PRIMARY KEY (idDelivery, idOrder),
    CONSTRAINT fk_delivery_order FOREIGN KEY (idOrder) REFERENCES request(idOrder) ON UPDATE CASCADE
) ENGINE=InnoDB""")

TABLES["warehouse"] = ("""
    CREATE TABLE IF NOT EXISTS warehouse (
	idWarehouse INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR (255),
    quantity INT DEFAULT 0    
) ENGINE=InnoDB""")

TABLES["provider"] = ("""
CREATE TABLE IF NOT EXISTS provider (
	idProvider INT AUTO_INCREMENT PRIMARY KEY,
    prov_name VARCHAR(255),
    cnpj CHAR(15) NOT NULL,
    email VARCHAR(75) NOT NULL,
    phone CHAR(11),
    CONSTRAINT cnpj_unique UNIQUE (cnpj)
) ENGINE=InnoDB""")

TABLES["seller"] = ("""
CREATE TABLE IF NOT EXISTS seller (
	idSeller INT AUTO_INCREMENT PRIMARY KEY,
    seller_name VARCHAR(255),
    cnpj CHAR(15),
    cpf CHAR(11),
    email VARCHAR(75) NOT NULL,
    phone CHAR(11),
    CONSTRAINT cnpj_unique UNIQUE (cnpj),
    CONSTRAINT cpf_unique UNIQUE (cpf)
) ENGINE=InnoDB""")

TABLES["product"] = ("""
CREATE TABLE IF NOT EXISTS productBySeller (
	idSeller INT,
    idProduct INT,
    quantity INT DEFAULT 1,
    PRIMARY KEY (idSeller, idProduct),
    CONSTRAINT fk_product_seller FOREIGN KEY (idSeller) REFERENCES seller(idSeller) ON UPDATE CASCADE,
    CONSTRAINT fk_product FOREIGN KEY (idProduct) REFERENCES product(idProduct) ON UPDATE CASCADE
) ENGINE=InnoDB""")

TABLES["providerByProduct"] = ("""
CREATE TABLE IF NOT EXISTS providerByProduct (
	idProvider INT,
    idProduct INT,
    PRIMARY KEY (idProvider, idProduct),
    CONSTRAINT fk_product_provider FOREIGN KEY (idProvider) REFERENCES provider(idProvider) ON UPDATE CASCADE,
    CONSTRAINT fk_productByProvider FOREIGN KEY (idProduct) REFERENCES product(idProduct) ON UPDATE CASCADE
) ENGINE=InnoDB""")

TABLES["productByRequest"] = ("""
CREATE TABLE IF NOT EXISTS productByRequest (
	idOrder INT,
    idProduct INT,
    quantity INT DEFAULT 1,
    stock_status ENUM ("Available", "Out of Stock") DEFAULT "Available",
    PRIMARY KEY (idOrder, idProduct),
    CONSTRAINT fk_request_product FOREIGN KEY (idOrder) REFERENCES request(idOrder) ON UPDATE CASCADE,
    CONSTRAINT fk_product_order FOREIGN KEY (idProduct) REFERENCES product(idProduct) ON UPDATE CASCADE
) ENGINE=InnoDB""")

TABLES["productByStock"] = ("""
CREATE TABLE IF NOT EXISTS productByStock (
	idStock INT,
    idProduct INT,
    quantity INT DEFAULT 1,
    PRIMARY KEY (idStock, idProduct),
    CONSTRAINT fk_stockqntt FOREIGN KEY (idStock) REFERENCES warehouse(idWarehouse) ON UPDATE CASCADE,
    CONSTRAINT fk_product_warehouse FOREIGN KEY (idProduct) REFERENCES product(idProduct) ON UPDATE CASCADE
) ENGINE=InnoDB""")

