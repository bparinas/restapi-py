from flask import Flask, jsonify, request

from http import HTTPStatus

app = Flask(__name__)

events = [
    {
        'id': 1,
        'event_name': 'Birthday',
        'event_location': 'Tokyo',
        'starttime': '10:00',
        'endtime': '12:00',
        'rsvp_email': 'user1@example.com'
    },
    {
        'id': 2,
        'event_name': 'Reunion',
        'event_location': 'Osaka',
        'starttime': '15:00',
        'endtime': '21:00',
        'rsvp_email': 'user2@example.com'
    }
]

@app.route('/events/', methods=['GET'])

#list events
def get_events():

    return jsonify({'data': events})

@app.route('/events/<int:event_id>', methods=['GET'])

#list specific event
def get_event(event_id):

    event = next((event for event in events if event['id'] == event_id), None)

    if event:
        return jsonify(event)
        
    return jsonify({'message': 'event not found'}), HTTPStatus.NOT_FOUND

@app.route('/events', methods=['POST'])

#sign-up event
def signup_event():

    data = request.get_json()

    name = data.get('event_name')
    location = data.get('event_location')
    start_time = data.get('starttime')
    end_time = data.get('endtime')
    email = data.get('rsvp_email')
    

    event = {
        'id': len(events) + 1,
        'event_name': name,
        'event_location': location,
        'starttime': start_time,
        'endtime': end_time,
        'rsvp_email': email
    }

    events.append(event)
    return jsonify(event), HTTPStatus.CREATED

@app.route('/events/<int:event_id>', methods=['PUT'])

#update event record
def update_event(event_id):

    event = next((event for event in events if event['id'] == event_id), None)

    if not event:
        return jsonify({'message': 'event not found'}), HTTPStatus.NOT_FOUND
        
    data = request.get_json()
    event.update(
        {
            'event_name': data.get('event_name'),
            'event_location': data.get('event_location'),
            'starttime': data.get('starttime'),
            'endtime': data.get('endtime'),
            'rsvp_email': data.get('rsvp_email')
        }
    )
    return jsonify(event)

@app.route('/events/<int:event_id>', methods=['DELETE'])

#delete particular event 
def delete_event(event_id):

    event = next((event for event in events if event['id'] == event_id), None)

    if not event:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

    events.remove(event)
    return '', HTTPStatus.NO_CONTENT

if __name__ == '__main__':

    app.run()
