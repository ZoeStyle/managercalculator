from datetime import date
from uptime import uptime
from src.api import app, request_data
from src.domain.handlers.bhaskara_handler import bhaskara_handle


@app.route("/1/healthcheck", methods=['GET'])
async def read_root():
    return {
        'uptime': uptime(),
        'message': 'Ok',
        'date': date.today()
    }


@app.route('/1/bhaskara', methods=['POST'])
async def test_bhaskara():
    post_data = request_data.get_json()
    result = bhaskara_handle(post_data, uptime())

    if result['status']:
        return result, 200

    return result, 400
