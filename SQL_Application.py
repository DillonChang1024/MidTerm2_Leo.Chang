import mysql.connector

# Question1
# part2_step1
db = mysql.connector.connect(
  host="54.201.140.239",
  user="midterm",
  password="midtermBatch#1",
  database="midterm"
)

# Creating a cursor to execute SQL queries

SELECT first_name, last_name, patient_id, gender, height, weight, \
    pa.post_code FROM patient AS pa \
    JOIN district AS di \
    ON di.post_code = pa.post_code \
    AND di.district = 'Xinyi';
ursor.execute(sql)
    result = cursor.fetchall()
    for x in (0, len(result)-1):
        print(f"{result[x]['first_name']}, {result[x]['last_name']}, (No.{result[x]['patient_id']}), {result[x]['gender']}, Height: {result[x]['height']} cm, Weight: {result[x]['weight']} kg")