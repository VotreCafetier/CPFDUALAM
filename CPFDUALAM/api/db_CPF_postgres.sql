create table city (
    city_id serial primary key,
    city_name varchar unique not null
);
create table country (
    country_id serial primary key,
    country_name varchar unique not null
);
create table province (
    province_id serial primary key,
    province_name varchar unique not null
);
create table color (
    color_id serial primary key,
    color_name varchar unique not null
);
create table orderstatus (
    status_id serial primary key,
    status_name varchar unique not null
);
create table paiement (
    paiement_id serial primary key,
    card_number bigint unique not null,
    expiration_date smallint not null,
    ccv smallint not null
);
create table product (
    product_id serial primary key,
    product_name varchar not null,
    product_price decimal(16,2) not null,
    color_id int not null references color ON DELETE CASCADE,
    product_stock int default '0',
    product_model varchar,
    product_description varchar,
    product_year_guaranteed smallint,
    product_tech_sheet_url varchar
);
create table client (
    client_id serial primary key,
    client_name varchar not null,
    client_lastname varchar not null,
    client_email varchar unique not null,
    address_1 varchar not null,
    address_2 varchar,
    postal_code nchar(6) not null,
    client_phone bigint,
    creation_date timestamp not null default now(),
    country_id int not null references country ON DELETE CASCADE,
    city_id int not null references city ON DELETE CASCADE,
    province_id int not null references province ON DELETE CASCADE,
    paiement_id int not null references paiement ON DELETE CASCADE
);
create table client_order (
    order_id serial primary key,
    client_id int not null references client ON DELETE CASCADE,
    product_id int not null references product ON DELETE CASCADE,
    nbr_product_ordered int default 1,
    order_date timestamp not null,
    shipping_date timestamp,
    status_id int not null references orderstatus ON DELETE CASCADE,
    comments varchar
);

/* index section */
/* create index at each joint (where there is a foreign key) */


create index fk_color_id on product (color_id);
create index fk_order_product on client_order (product_id,client_id,status_id);
create index fk_client_country on client (country_id,city_id,province_id,paiement_id);