import socket
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/healthy_check')
def healthy_check():
    pod = socket.gethostname()
    ip = socket.gethostbyname(pod)
    return 'I am fine! <pod: {}, ip: {}>'.format(pod, ip)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
