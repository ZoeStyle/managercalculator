from datetime import date
from uptime import uptime
from typing import Any
from flask import Flask
from src.domain.handlers.bhaskara_handler import bhaskara_handle
from os import environ

app = Flask(__name__)


@app.route("/1/healthcheck", methods=['GET'])
async def read_root():
    return {
        'uptime': uptime(),
        'message': 'Ok',
        'date': date.today()
    }


@app.route('/1/bhaskara', methods=['POST'])
async def test_bhaskara(request: dict[str, Any]):
    return bhaskara_handle(request)

if __name__ == "__main__":
    try:
        port = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        port = 5555

    host = environ.get('SERVER_HOST', 'localhost')
    app.run(host=host, port=port)
