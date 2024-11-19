# Para realizar a simulação dos dados, iremos utilizar a biblioteca random para gerar números aleatórios.
# Itens para serem ilustrados para o usuário:
#   1. Status atual de funcionamento
#   2. Última data de atualização
#   3. Qual é a configuração atual de monitoramento?

from logger import logger
from turbine import Turbine
import xlsxwriter

# Lista de objetos contendo a classe Turbina
turbines = [Turbine(1, True), Turbine(2, True), Turbine(3, False)]

# Define o status de operação da máquina
operation_status = True

logger.info('HyDrive - Monitoring System | Starting..')
logger.info(f'Operation Status - Machine: {operation_status}')
for turbine in turbines:
    if turbine.status:
        logger.info(f'Turbine {turbine.index} operation status: {turbine.status}')
    else:
        logger.warning(f'Turbine {turbine.index} operation status: {turbine.status}')