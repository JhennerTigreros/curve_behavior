copy dates from '<<S3_BUCKET>>/date.csv'
credentials '<<IAM_ROLE>>'
delimiter '|' region 'us-east-2';

copy origins from '<<S3_BUCKET>>/locations.csv'
credentials '<<IAM_ROLE>>'
delimiter '|' region 'us-east-2';

copy employment from '<<S3_BUCKET>>/employment.csv'
credentials '<<IAM_ROLE>>'
delimiter '|' region 'us-east-2';

copy economy from '<<S3_BUCKET>>/economy.csv'
credentials '<<IAM_ROLE>>'
delimiter '|' region 'us-east-2';

copy news from '<<S3_BUCKET>>/news.csv'
credentials '<<IAM_ROLE>>'
delimiter '|' region 'us-east-2';

copy tweets from '<<S3_BUCKET>>/tweets.csv'
credentials '<<IAM_ROLE>>'
delimiter '|' region 'us-east-2';

copy tests from '<<S3_BUCKET>>/test.csv'
credentials '<<IAM_ROLE>>'
delimiter '|' region 'us-east-2';

copy cases from '<<S3_BUCKET>>/cases.csv'
credentials '<<IAM_ROLE>>'
delimiter '|' region 'us-east-2';