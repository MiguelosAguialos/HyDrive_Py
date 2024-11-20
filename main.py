# O programa atual possui funcionalidades primordias de ilustrar os dados capturados pelas turbinas (simulados), histórico, geração de relatório por dia e agendamento.

from hist import create_hist_file, read_hist
from main_exception import MainException
from report import generate_report
from turbine import *
import schedule
import time

# Lista de objetos contendo a classe Turbina
turbines = [Turbine(1, True), Turbine(2, True), Turbine(3, False)]

# Define o status de operação da máquina
operation_status = True

# Define o intervalo de valores aleatórios que serão gerados com base em um mínimo e máximo apresentados (velocidade da água)
speed_interval = (0.5, 2.0)

# Script principal
def script():
    logger.info('HyDrive - Monitoring System | Starting..')
    logger.info(f'Operation Status - Machine: {operation_status}')
    show_status_turbines(turbines)
    generate_speed_power_turbines(turbines, speed_interval)

    date = create_hist_file(get_str_turbines(turbines))
    data = read_hist(date)
    generate_report(data)

# Função para executar o agendamento com tratamento de exceções personalizadas
def execute(opt, interval):
    # Biblioteca de agendamento simples para definir o período de monitoramento que o usuário desejar.
    # Possíveis configurações: sec (segundos), min (minutos), hour (horas). Além disso, é possível definir o intervalo de tempo do agendamento com base no tipo escolhido

    script()
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
    execute(input("Escolha o tipo de agendamento (padrão em horas): \n'sec': segundos\n'min': minutos\n-> "),
            float(input('Digite o intervalo de tempo desejado\n-> ')))
except MainException as e:
    logger.error(e.msg)



