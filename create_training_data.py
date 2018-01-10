import sqlite3
import pandas as pd
df = 'movie_quotes'
connection = sqlite3.connect('{}.db'.format(df))

df = pd.read_sql("SELECT * FROM quotes", connection)
# print (len(df))
test = df[:5000]
train = df[5000:]

# print (len(test))
# print (len(train))

with open("test.from", "a", encoding='utf-8') as f:
	for content in test['title'].values:
		f.write(content+'\n')

with open("train.from", "a", encoding='utf-8') as f:
	for content in train['title'].values:
		f.write(content+'\n')