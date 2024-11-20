# Classe de model e service para a Turbina

import datetime
from common_codes import get_power, generate_random_values
from logger import logger

class Turbine:
    # Declaração do objeto Turbine
    def __init__(self, index, status):
        self.index = index
        self.status = status
        self.speed = 0
        self.power = 0

    # função para adequar o objeto em texto para o histórico
    def __to_string__(self):
        date = datetime.datetime.now()
        format_date = (date.strftime('%d') + '/' + date.strftime('%m') + '/' + date.strftime('%Y') + ' ' +
                       date.strftime('%H') + ':' + date.strftime('%M') + ':' + date.strftime('%S'))
        return f'{format_date};{self.index};{self.status};{self.speed};{self.power}'

# Função para mostrar no console o status de cada turbina
def show_status_turbines(turbines):
    for turbine in turbines:
        if turbine.status:
            logger.info(f'Turbine {turbine.index} operation status: {turbine.status}')
        else:
            logger.warning(f'Turbine {turbine.index} operation status: {turbine.status}')

# Função para adicionar a velocidade da água e a potência no objeto turbina
def add_speed_power_turbine(speed, power, turbine):
    turbine.speed = speed
    turbine.power = power

# Função com a finalidade de utilizar a função acima e ilustrar esses valores no console
def generate_speed_power_turbines(turbines, intervalo):
    for turbine in turbines:
        if turbine.status:
            speed = generate_random_values(intervalo)
            add_speed_power_turbine(speed, get_power(speed), turbine)
            logger.info(f'Turbine {turbine.index} | Water speed in m/s: {turbine.speed} | Power: {turbine.power}')

# Função para o gerar o texto das turbinas e armazená-lo no histórico
def get_str_turbines(turbines):
    text = ''
    for turbine in turbines:
        text += Turbine.__to_string__(turbine) + ';\n'
    return text