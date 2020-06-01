#本代码实现功能：登陆本地mysql

from sqlalchemy import create_engine
import pandas as pd
class Log_on_MySQL(object):
    def __init__(self,host,port,db,user,password):
        self.host = host
        self.port = str(port)
        self.db = db
        self.user = user
        self.password = str(password)
        self.path = 'mysql://' + self.user + ':' + self.password + '@' + self.host + ':' + self.port + '/' + self.db

    def log_on_mysql(self):
        self.engine_ts = create_engine(self.path)
        return self.engine_ts

    def read_date(self,sql):
        self.sql = sql
        self.df = pd.read_sql_query(self.sql, self.log_on_mysql())
        return self.df

    def write_data(self):
        self.tablename
        self.df
        self.df.to_sql(self.tablename,self.log_on_mysql(),index=False,if_exists='replace',chunksize=5000)
        #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html





