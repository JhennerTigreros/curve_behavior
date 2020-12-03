create table dates(
    date_id smallint not null distkey sortkey,
    cal_date date not null ENCODE delta,
    day character(3) not null ENCODE bytedict,
    month character(5) not null ENCODE bytedict,
    year smallint not null ENCODE bytedict,
    qtr character(5) not null ENCODE runlength
);

create table origins(
    origin_id smallint not null distkey sortkey,
    origin varchar(100) not null ENCODE bytedict,
);

create table employment(
    employment_id smallint not null distkey,
    tgp NUMERIC ENCODE mostly8,
    "to" NUMERIC ENCODE mostly8,,
    td NUMERIC ENCODE mostly8,,
    ocupados NUMERIC ENCODE mostly16,
    desocupados NUMERIC ENCODE mostly16,
    inactivos NUMERIC ENCODE mostly16,
    date_id smallint not null sortkey
);

create table economy(
    economy_id smallint not null distkey,
    inflacion_total decimal(5,3) not null ENCODE az64,
    limite_superior smallint not null ENCODE bytedict,
    meta_inflacion smallint not null ENCODE bytedict,
    limite_inferior smallint not null ENCODE bytedict,
    date_id smallint not null sortkey
);

create table news(
    news_id smallint not null distkey,
    titulo text not null ENCODE lzo,
    categoria varchar(100) not null ENCODE bytedict,
    resumen text not null ENCODE lzo,
    date_id smallint not null sortkey
);

create table tweets(
    tweet_id smallint not null distkey,
    texto text not null ENCODE text32k,
    date_id smallint not null sortkey
);

create table tests(
    test_id smallint not null distkey,
    cantidad decimal(10, 3) not null ENCODE az64,
    date_id smallint sortkey,
    origin_id smallint
);

create table cases(
    case_id int not null distkey,
    edad smallint ENCODE delta,
    sexo char(1) ENCODE bytedict,
    fuente_tipo_contagio varchar(50) ENCODE runlength,
    ubicacion varchar(30) ENCODE bytedict,
    estado varchar(30) ENCODE runlength,
    recuperado varchar(30) ENCODE bytedict,
    tipo_recuperacion varchar(30) ENCODE runlength,
    date_symptoms_id smallint,
    date_dead_id smallint,
    date_diagnosis_id smallint sortkey,
    date_recovered_id smallint,
    origin_id smallint
);