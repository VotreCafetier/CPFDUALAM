CREATE TABLE City (
    City_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    City_Name NVARCHAR UNIQUE NOT NULL
);
CREATE TABLE Country (
    Country_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Country_Name NVARCHAR UNIQUE NOT NULL
);
CREATE TABLE Province (
    Province_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Province_Name NVARCHAR UNIQUE NOT NULL
);
CREATE TABLE Color (
    Color_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Color_Name NVARCHAR UNIQUE NOT NULL
);
CREATE TABLE OrderStatus (
    Status_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Status_Name NVARCHAR UNIQUE NOT NULL
);
CREATE TABLE Paiement (
    Paiement_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Card_Number TINYINTEGER UNIQUE NOT NULL,
    Expiration_Date TINYINTEGER NOT NULL,
    CCV TINYINTEGER NOT NULL
);
CREATE TABLE Product (
    Product_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Product_Name NVARCHAR NOT NULL,
    Product_Price DECIMAL(16,2) NOT NULL,
    Color_ID INTEGER NOT NULL,
    Product_Stock INTEGER DEFAULT 0,
    Product_Model NVARCHAR DEFAULT '',
    Product_Description NVARCHAR DEFAULT '',
    Product_Year_Guaranteed TINYINTEGER DEFAULT 0,
    Product_Tech_Sheet_URL NVARCHAR,

    FOREIGN KEY (Color_ID) REFERENCES Color(Color_ID)
);
CREATE TABLE Client (
    Client_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Client_Name NVARCHAR NOT NULL,
    Client_LastName NVARCHAR NOT NULL,
    Client_Email NVARCHAR UNIQUE NOT NULL,
    Address_1 NVARCHAR NOT NULL,
    Address_2 NVARCHAR,
    Postal_Code NCHAR(6) NOT NULL,
    Client_Phone TINYINTEGER,
    Creation_Date DATETIME NOT NULL,
    Country_ID INTEGER NOT NULL,
    City_ID INTEGER NOT NULL,
    Province_ID INTEGER NOT NULL,
    Paiement_ID INTEGER,

    FOREIGN KEY (Country_ID) REFERENCES Country(Country_ID),
    FOREIGN KEY (City_ID) REFERENCES City(City_ID),
    FOREIGN KEY (Province_ID) REFERENCES Province(Province_ID),
    FOREIGN KEY (Paiement_ID) REFERENCES Paiement(Paiement_ID)
);
CREATE TABLE Client_Order (
    Order_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Client_ID INTEGER NOT NULL,
    Product_ID INTEGER NOT NULL,
    Order_Date DATETIME NOT NULL,
    Shipping_Date DATETIME,
    Status_ID INTEGER NOT NULL,
    Comments NVARCHAR,

    FOREIGN KEY (Client_ID) REFERENCES Client(Client_ID),
    FOREIGN KEY (Status_ID) REFERENCES OrderStatus(Status_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);

/* Index Section */
/* Create index at each joINTEGER (where there is a foreign key) */

CREATE INDEX FK_Color_ID ON Product(Color_ID);
CREATE INDEX FK_Order_Product_ID ON Client_Order(Product_ID);
CREATE INDEX FK_Order_Client_ID ON Client_Order(Client_ID);
CREATE INDEX FK_Order_Status_ID ON Client_Order(Status_ID);
CREATE INDEX FK_Client_Country_ID ON Client(Country_ID);
CREATE INDEX FK_Client_City_ID ON Client(City_ID);
CREATE INDEX FK_Client_Province_ID ON Client(Province_ID);
CREATE INDEX FK_Client_Paiement_ID ON Client(Paiement_ID);

/* Index on important unique key */
CREATE UNIQUE INDEX UK_EMAIL ON Client(Client_Email);
CREATE UNIQUE INDEX UK_Color_Name ON Color(Color_Name);
CREATE UNIQUE INDEX UK_Status_Name ON OrderStatus(Status_Name);
CREATE UNIQUE INDEX UK_CardNumber ON Paiement(Card_Number);
CREATE UNIQUE INDEX UK_ProvinceName ON Province(Province_Name);
CREATE UNIQUE INDEX UK_CityName ON City(City_Name);
CREATE UNIQUE INDEX UK_CountryName ON Country(Country_Name);