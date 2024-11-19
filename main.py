# Para realizar a simulação dos dados, iremos utilizar a biblioteca random para gerar números aleatórios.
# Itens para serem ilustrados para o usuário:
#   1. Status atual de funcionamento
#   2. Última data de atualização
#   3. Qual é a configuração atual de monitoramento?

from logger import logger
import xlsxwriter

logger.info('HyDrive - Monitoring System | Starting..')