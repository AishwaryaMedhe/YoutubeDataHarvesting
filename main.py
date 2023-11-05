import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dreamer_1',
    port='3306',
    database='project_data'
)
mycursor =mydb.cursor()
channel1 = "create table channel( channel_id VARCHAR,channel_name VARCHAR,channel_type VARCHAR,channel_views INT)"
mycursor.execute(channel1)
print('table created')

