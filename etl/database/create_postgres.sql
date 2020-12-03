create table dates(
    date_id smallint not null,
    cal_date date not null,
    day character(3) not null,
    month character(5) not null,
    year smallint not null,
    qtr character(5) not null
);

create table origins(
    origin_id smallint not null,
    origin varchar(100) not null
);

create table employment(
    employment_id smallint not null,
    tgp NUMERIC,
    "to" NUMERIC,
    td NUMERIC,
    ocupados NUMERIC,
    desocupados NUMERIC,
    inactivos NUMERIC,
    date_id smallint not null
);

create table economy(
    economy_id smallint not null,
    inflacion_total decimal(5,3) not null,
    limite_superior smallint not null,
    meta_inflacion smallint not null,
    limite_inferior smallint not null,
    date_id smallint not null
);

create table news(
    news_id smallint not null,
    titulo text not null,
    categoria varchar(100) not null,
    resumen text not null,
    date_id smallint not null
);

create table tweets(
    tweet_id smallint not null,
    texto text not null,
    date_id smallint not null
);

create table tests(
    test_id smallint not null,
    cantidad decimal(10, 3) not null,
    date_id smallint,
    origin_id smallint
);

create table cases(
    case_id int not null,
    edad smallint,
    sexo char(1),
    fuente_tipo_contagio varchar(50),
    ubicacion varchar(30),
    estado varchar(30),
    recuperado varchar(30),
    tipo_recuperacion varchar(30),
    date_symptoms_id smallint,
    date_dead_id smallint,
    date_diagnosis_id smallint,
    date_recovered_id smallint,
    origin_id smallint
);