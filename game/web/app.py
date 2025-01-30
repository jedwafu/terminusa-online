from flask import Flask, render_template
from flask_socketio import SocketIO
from game.blockchain.nft_manager import NFTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('terminal.html')

@socketio.on('command')
def handle_command(cmd):
    # Command processing logic
    response = process_command(cmd)
    socketio.emit('output', response)