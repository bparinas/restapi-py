from flask import Flask, jsonify, request
from http import HTTPStatus
import sqlite3
import json
import collections

app = Flask(__name__)



@app.route('/events/', methods=['GET'])

#list events
def get_events():
   with sqlite3.connect("events.db") as conn:
      cur = conn.cursor()
      cur.execute("SELECT * FROM events")
      rows = cur.fetchall()
        
      obj_list = []
      for row in rows:
         d = collections.OrderedDict()
         d["id"] = row[0]
         d["event_name"] = row[1]
         d["event_location"] = row[2]
         d["starttime"] = row[3]
         d["endtime"] = row[4]
         d["rsvp_email"] = row[5]
         obj_list.append(d)

      return jsonify({'data': obj_list})
      con.close()
