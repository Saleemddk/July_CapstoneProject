import pandas as pd
import json
from sqlalchemy import create_engine,text

# create mysql database commection
mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/enterpriseretaildwh')


def filter_sales_data():
    query=text("""SELECT * FROM staging_sales where sale_date>='2024-09-05'""")
    df = pd.read_sql(query,mysql_engine)
    df.to_sql('filtered_sales',mysql_engine,if_exists='replace',index=False)

if __name__=="__main__":
    filter_sales_data()

    