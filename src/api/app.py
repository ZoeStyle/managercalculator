from datetime import date
from uptime import uptime
from flask import Flask, request
from src.domain.handlers.bhaskara_handler import bhaskara_handle

app = Flask(__name__)


@app.route("/1/healthcheck", methods=['GET'])
async def read_root():
    return {
        'uptime': uptime(),
        'message': 'Ok',
        'date': date.today()
    }


@app.route('/1/bhaskara', methods=['POST'])
async def test_bhaskara():
    return bhaskara_handle(request.get_json())

if __name__ == "__main__":
    host = '0.0.0.0'
    app.run(host=host)
