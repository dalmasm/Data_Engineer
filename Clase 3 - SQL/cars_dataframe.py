import pandas as pd
import sqlite3

orig_file=pd.read_csv("C:\\Documentos\\Data Engineer\\Clase 3 - SQL\\auto.csv" )

df_cars=pd.DataFrame(orig_file)

df_cars.head()

conn = sqlite3.connect("C:\Documentos\Data Engineer\Clase 3 - SQL\cars_df_base.db")

df_cars.to_sql('cars', conn, index=False, if_exists='replace')

conn.close()

