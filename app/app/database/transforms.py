import sqlite3
import pandas as pd

conn = sqlite3.connect(r"/app/app/database/wine_data.sqlite")
c = conn.cursor()

df = pd.read_sql("select * from wine_data", conn)

df = df[['country', 'description', 'rating', 'price', 'province', 'title', 'variety', 'winery', 'color', 'varietyID']]
