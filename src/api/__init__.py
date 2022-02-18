from flask import Flask, request

app = Flask(__name__)
request_data = request

import src.api.bhaskara_route
import src.api.healthcheck_route