from datetime import date
from typing import Any
from src.domain.entities.equation import equation


def check_key(dict: dict[str, Any], key: str) -> bool:
    return key in dict


def is_valid_parameters(dict: dict[str, Any]) -> bool:
    valueA = check_key(dict, 'valueA')
    valueB = check_key(dict, 'valueB')
    valueC = check_key(dict, 'valueC')
    return valueA and valueB and valueC


def is_valid_request(dict: dict[str, Any]) -> bool:
    return bool(dict)


def assemble_equation(valueA: float, valueB: float,
                      valueC: float) -> dict[str, Any]:
    return equation(valueA, valueB, valueC)


def bhaskara_handle(req: dict[str, Any]) -> dict[str, Any]:
    if is_valid_request(req):
        if is_valid_parameters(req):
            return assemble_equation(
                req['valueA'], req['valueB'], req['valueC'])
        else:
            msg = {
                'status': False,
                'date': date.today(),
                'message': 'It is necessary to inform something in the request'
            }
        return msg
    else:
        msg = {
            'status': False,
            'date': date.today(),
            'message':
                'It is mandatory to inform the valueA and valueB and valueC'
        }
        return msg
