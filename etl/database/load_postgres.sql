copy dates from '<<LOCAL_PATH>>/date.csv'
delimiter '|' CSV HEADER;

copy origins from '<<LOCAL_PATH>>/locations.csv'
delimiter '|' CSV HEADER;

copy employment from '<<LOCAL_PATH>>/employment.csv'
delimiter '|' CSV HEADER;

copy economy from '<<LOCAL_PATH>>/economy.csv'
delimiter '|' CSV HEADER;

copy news from '<<LOCAL_PATH>>/news.csv'
delimiter '|' CSV HEADER;

copy tweets from '<<LOCAL_PATH>>/tweets.csv'
delimiter '|' CSV HEADER;

copy tests from '<<LOCAL_PATH>>/test.csv'
delimiter '|' CSV HEADER;

copy cases from '<<LOCAL_PATH>>/cases.csv'
delimiter '|' CSV HEADER;