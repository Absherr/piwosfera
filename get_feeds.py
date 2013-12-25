import sqlite3
import feedparser
import datetime

conn = sqlite3.connect('db.db')
c = conn.cursor()
entry_cursor = conn.cursor()
blog_list=list(c.execute('SELECT * FROM main_blog'))
for row in blog_list:
	print row
	feed = feedparser.parse(row[3])
	
	for entry in feed['items']:
		entry_title = entry['title']
		print entry_title
		entry_cursor.execute('SELECT * FROM main_entry WHERE title="'+entry_title+'"')
		
		if entry_cursor.fetchone() is None:
			date = entry['updated_parsed']
			dt = datetime.datetime(year = date[0], month = date[1], day=date[2], hour=date[3], minute=date[4], second=date[5])
		
			query = 'INSERT INTO main_entry ("title","date","address","blog_id") VALUES ("'+entry['title']+'","'+str(dt)+'","'+entry['link']+'","'+str(row[0])+'")'
			c.execute(query)
	conn.commit()
conn.close()
