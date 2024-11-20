# Para realizar a simulação dos dados, iremos utilizar a biblioteca random para gerar números aleatórios.
# Itens para serem ilustrados para o usuário:
#   1. Status atual de funcionamento
#   2. Última data de atualização
#   3. Qual é a configuração atual de monitoramento?
from main_exception import MainException
from report import generate_report
from turbine import *
import schedule
import time

# Lista de objetos contendo a classe Turbina
turbines = [Turbine(1, True), Turbine(2, True), Turbine(3, False)]

# Escolha de monitoramento para monitoramento por segundo, minuto ou hora.
tempo_monitoramento = 'sec'

# Define o status de operação da máquina
operation_status = True

def script():
    logger.info('HyDrive - Monitoring System | Starting..')
    logger.info(f'Operation Status - Machine: {operation_status}')
    show_status_turbines(turbines)
    generate_report('Olá')

def execute(opt, interval):
    # Biblioteca de agendamento simples para definir o período de monitoramento que o usuário desejar.
    # POssíveis configurações: sec (segundos), min (minutos), hour (horas). Além disso, é possível definir o intervalo de tempo do agendamento com base no tipo escolhido

    try:
        if interval == 1:
            if opt == 'sec':
                schedule.every().second.do(script)
            elif opt == 'min':
                schedule.every().minute.do(script)
            else:
                schedule.every().hour.do(script)
        elif interval <= 0:
            raise MainException('Tempo de intervalo inválido!')
        else:
            if opt == 'sec':
                schedule.every(interval).seconds.do(script)
            elif opt == 'min':
                schedule.every(interval).minutes.do(script)
            else:
                schedule.every(interval).hours.do(script)
    except MainException as err:
        raise MainException(err.msg)
    except Exception as err:
        raise MainException(f'Ocorreu um erro durante a configuração do agendamento: {err}')

    while True:
        schedule.run_pending()
        time.sleep(1)

try:
    script()
    execute('min', '-1')
except MainException as e:
    logger.error(e.msg)



