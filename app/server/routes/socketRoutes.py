from flask_socketio import emit
from app import socketio


@socketio.on('connect')
def test_connect():
    print('Client connected')
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
    emit('my response', {'data': 'Disconnected'})


@socketio.on('message')
def handle_message(message):
    print(f'Received message: {message}')
    emit('my response', {'data': message})
