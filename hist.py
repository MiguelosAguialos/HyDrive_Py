# Gera arquivo txt com informações de histórico para cada dia.

from common_codes import create_folder
import datetime

# Função que cria o arquivo de histórico com base no dia atual
def create_hist_file(data):
    create_folder('./hist')

    date = datetime.datetime.now()
    format_date = date.strftime('%d') + '-' + date.strftime('%m') + '-' + date.strftime('%Y')
    file = open(f'./hist/{format_date}.txt', 'a')
    file.write(data)
    file.close()
    return format_date

# Função que lê o arquivo de histórico baseado no dia atual e adequa o formato para o relatório
def read_hist(date):
    data = []
    file = open(f'./hist/{date}.txt', 'r')
    for line in file:
        split_line = line.split(';')
        split_line.pop()
        split_line[1] = float(split_line[1])
        split_line[3] = float(split_line[3])
        split_line[4] = float(split_line[4])
        data.append(split_line)
    return data



