from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print('Received message: ' + str(data))
    emit('response', {'data': 'Server received: ' + str(data)})

if __name__ == '__main__':
    socketio.run(app, debug=True)
