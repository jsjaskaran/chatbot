import sqlite3, json
from datetime import datetime

df = 'movie_quotes'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(df))
c = connection.cursor()

def transaction_bldr(sql):
	global sql_transaction
	sql_transaction.append(sql)
	if len(sql_transaction) > 1000:
		c.execute('BEGIN TRANSACTION')
		for s in sql_transaction:
			try:
				c.execute(s)
			except:
				pass
		connection.commit()
		sql_transaction = []

def sql_insert_row(title):
	try:
		sql = """INSERT INTO quotes(title) VALUES("{}")""".format(title)
		transaction_bldr(sql)
	except Exception as e:
		print ('Error insert: ', str(e))

def create_table():
	c.execute("""CREATE TABLE IF NOT EXISTS quotes(title TEXT)""")

if __name__ == '__main__':
	create_table()
	row_counter = 0

	with open("movie_lines.txt") as f:
		for item in f.readlines():
			row_counter += 1
			title = item.split('+++$+++')[-1].strip()
			sql_insert_row(title)
			if row_counter % 10000 == 0:
				print('Total rows read: {}, Time: {}'.format(row_counter, str(datetime.now())))