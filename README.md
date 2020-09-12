##Installation:
1. Create your python virtual environment
```
$ python3 -m venv pyapi
$ source pyapi/bin/activate
```

2. Clone this repository
```
$ git clone https://github.com/bparinas/restapi-py.git
$ cd restapi-py
```

2. Install latest flask and sqlite3
```
$ pip install sqlite3
$ pip install Flask
$ flask run --host=0.0.0.0 --port=8000
```

Use cases:

#Get all events
```
request:

curl -i -X GET http://34.70.25.201:8000/events

respond:
{
    "data": [{
        "endtime": "12:00",
        "event_location": "Tokyo",
        "event_name": "Birthday",
        "id": 1,
        "rsvp_email": "user1@example.com",
        "starttime": "10:00"
    }, {
        "endtime": "21:00",
        "event_location": "Osaka",
        "event_name": "Reunion",
        "id": 2,
        "rsvp_email": "user2@example.com",
        "starttime": "15:00"
    }]
}
```

#Get specific event details
```
request:
curl -i -X GET http://34.70.25.201:8000/events/1

respond:
{
    "endtime": "12:00",
    "event_location": "Tokyo",
    "event_name": "Birthday",
    "id": 1,
    "rsvp_email": "user1@example.com",
    "starttime": "10:00"
}
```

#Add/sign-up event
```
request:
curl -i -X POST http://34.70.25.201:8000/events -H "Content-Type: application/json" -d '{"event_name":"Conferences", "event_location":"Kyoto", "starttime":"09:00", "endtime":"17:00", "rsvp_email":"user3@example.com"}'

respond:
{
    "endtime": "17:00",
    "event_location": "Kyoto",
    "event_name": "Conferences",
    "id": 3,
    "rsvp_email": "user3@example.com",
    "starttime": "09:00"
}
```

#Update event details
```
request:
curl -i -X PUT http://34.70.25.201:8000/events/3 -H "Content-Type: application/json" -d '{"event_name":"Conferences", "event_location":"Kyoto", "starttime":"09:00", "endtime":"17:00", "rsvp_email":"user4@example.com"}'

respond:
{
    "endtime": "17:00",
    "event_location": "Kyoto",
    "event_name": "Conferences",
    "id": 3,
    "rsvp_email": "user4@example.com",
    "starttime": "09:00"
}

verify update:
curl -i -X GET http://34.70.25.201:8000/events/3

respond:
{
    "endtime": "17:00",
    "event_location": "Kyoto",
    "event_name": "Conferences",
    "id": 3,
    "rsvp_email": "user4@example.com",
    "starttime": "09:00"
}
```

#Delete event 3
```
request:
curl -i -X DELETE http://34.70.25.201:8000/events/3

respond:
HTTP/1.0 204 NO CONTENT
Content-Type: text/html; charset=utf-8

verify update (expected no event #3):
curl -i -X GET http://34.70.25.201:8000/events
```
