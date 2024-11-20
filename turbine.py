from common_codes import get_power, generate_random_values
from logger import logger
import common_codes

class Turbine:
    def __init__(self, index, status):
        self.index = index
        self.status = status
        self.speed = 0
        self.power = 0

def show_status_turbines(turbines):
    for turbine in turbines:
        if turbine.status:
            logger.info(f'Turbine {turbine.index} operation status: {turbine.status}')
        else:
            logger.warning(f'Turbine {turbine.index} operation status: {turbine.status}')

def add_speed_power_turbine(speed, power, turbine):
    turbine.speed = speed
    turbine.power = power

def generate_speed_power_turbines(turbines, intervalo):
    for turbine in turbines:
        if turbine.status:
            speed = generate_random_values(intervalo)
            add_speed_power_turbine(speed, get_power(speed), turbine)
            logger.info(f'Turbine {turbine.index} | Water speed in m/s: {turbine.speed} | Power: {turbine.power}')