from datetime import date
import math
from typing import Any
from src.logger.logger import error, info


def is_valid(valueA: float) -> bool:
    return valueA != 0


def validate_if_valueB_and_C_equal_to_0(valueB: float, valueC: float) -> bool:
    return valueB == 0 and valueC == 0


def validate_if_delta_is_less_than_0(delta: float) -> bool:
    return delta < 0


def delta(valueA: float, valueB: float, valueC: float) -> float:
    return (valueB * valueB) - (4 * valueA * valueC)


def _get_divisor(valueA) -> float:
    return (2 * valueA)


def _get_raiz(delta) -> float:
    return math.sqrt(delta)


def calculate_x(valueA: float, valueB: float, delta: float) -> dict[str, Any]:
    raiz = _get_raiz(delta)
    divisor = _get_divisor(valueA)

    x1 = (-valueB + raiz) / divisor
    x2 = (-valueB - raiz) / divisor

    x1 = round(x1, 2)
    x2 = round(x2, 2)

    return{
        'x1': x1,
        'x2': x2
    }


def equation(valueA: float, valueB: float, valueC: float,
             uptime: float) -> dict[str, Any]:
    if is_valid(valueA):
        value_delta = delta(valueA, valueB, valueC)

        if validate_if_delta_is_less_than_0(value_delta):
            msg = {
                'status': False,
                'date': date.today(),
                'message': 'The values entered are not real roots'
            }
            error(str(msg), uptime)
            return msg

        if validate_if_valueB_and_C_equal_to_0(valueB, valueC):
            msg = {
                'status': False,
                'date': date.today(),
                'message': 'ValueB and valueC are set to zero'
            }
            error(str(msg), uptime)
            return msg

        msg = {
            'status': True,
            'date': date.today(),
            'message': calculate_x(valueA, valueB, value_delta)
        }
        info(str(msg), uptime)
        return msg
    else:
        msg = {
            'status': False,
            'date': date.today(),
            'message': "It's not a quadratic equation!"
        }
        error(str(msg), uptime)
        return msg
