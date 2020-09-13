import sqlite3

con = sqlite3.connect('events.db')
cObj = con.cursor()

cObj.execute('CREATE TABLE events(id INTEGER PRIMARY KEY AUTOINCREMENT, event_name TEXT, event_location TEXT, event_starttime DATETIME, event_endtime DATETIME, rsvp_email TEXT)')
con.commit()

events = [(1,'Birthday','Tokyo','2020-09-09 10:00+08:00','2020-09-09 12:00+08:00','sephy@example.com'),
          (2,'Reunion','Osaka','2020-09-10 15:00+08:00','2020-09-10 21:00+08:00','yuna@example.com'), 
          (3,'Conferences','Kyoto','2020-09-11 09:00+08:00','2020-09-11 17:00+08:00','uriel@example.com')
         ]
cObj.executemany('INSERT INTO events VALUES(?,?,?,?,?,?);', events)

con.commit()
con.close()
