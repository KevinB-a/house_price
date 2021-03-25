import pandas as pd
import sys 
sys.path.insert(0, "/home/apprenant/simplon_project/house_price/") 
from src.d00_utils.mysql_utlis import mysql_connect, save_to_mysql

# After dowloading my csv and xlsx files, I read them with pandas
df = pd.read_csv(r"/home/apprenant/PycharmProjects/house_price/Data/train.csv")


#Create connection with mysqm
connect = mysql_connect()

# Save the table in mysql database
save_to_mysql(db_connect=connect,df_to_save=df,df_name='maison')

