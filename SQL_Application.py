import time
import pymysql

# Question1
# part2_step1
db_settings = {
    "host": "54.201.140.239",
    "port": 3306,
    "user": "midterm",
    "password": "midtermBatch#1",
    "db": "midterm",
    "charset": "utf8"
}
# Creating a cursor to execute SQL queries
# Enable autocommit to automatically save
conn = pymysql.connect(**db_settings, autocommit=True)

with conn.cursor(pymysql.cursors.DictCursor) as cursor:

    # Write a python script to Show the information of patient who live in "Xinyi" district.
    sql = "SELECT first_name, last_name, patient_id, gender, height, weight, \
    pa.post_code FROM patient AS pa \
    JOIN district AS di \
    ON di.post_code = pa.post_code \
    AND di.district = 'Xinyi';"

    cursor.execute(sql)
    result = cursor.fetchall()
    # Expected Output:
    for x in (0, len(result)-1):
        print(f"{result[x]['first_name']}, {result[x]['last_name']}, (No.{result[x]['patient_id']}), {result[x]['gender']}, Height: {result[x]['height']} cm, Weight: {result[x]['weight']} kg")

    # close db
    conn.close()