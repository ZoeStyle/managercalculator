from datetime import date
from uptime import uptime
from src.api import app


@app.route("/1/healthcheck", methods=['GET'])
async def read_root():
    return {
        'uptime': uptime(),
        'message': 'Ok',
        'date': date.today()
    }
