# Arquivo para definir as funções diretamente relacionadas ao relatório em XLSX

import xlsxwriter
from xlsxwriter.utility import xl_range
import datetime
from common_codes import create_folder

columns = [
    {
        'header':'Data',
        'total_string':'Total'
    },
    {'header':'Num Turbina'},
    {'header':'Operação'},
    {'header':'Vel Água (m/s)'},
    {
        'header':'Potência (W)',
        'total_function':'sum'
    },
]

# Função para criar um título personalizado na planilha
def create_title(wb, ws):
    title_format = wb.add_format({'bold': True})
    title_format.set_size(14)
    title_format.set_align('center')
    title_format.set_valign('vcenter')
    title_format.set_font_color('#2C6FC3')
    ws.merge_range('C2:F4', 'HyDrive - Monitoring System', title_format)
    date = datetime.datetime.now()
    format_date = date.strftime('%d') + '/' + date.strftime('%m') + '/' + date.strftime('%Y')
    ws.write('G2', 'Classificação: Restrito', wb.add_format({'bold': True}))
    ws.write('G3', f'Última atualização: {format_date}', wb.add_format({'bold': True}))
    ws.write('G4', 'Versão: 1.0', wb.add_format({'bold': True}))
    ws.merge_range('B2:B4', '', title_format)
    ws.embed_image('B2', './images/report_icon.png', options={'x_scale': 0.1, 'y_scale': 0.1})

# Função para gerar o relatório com as linhas sendo o parâmetro
def generate_report(data):
    create_folder('./reports')
    date = datetime.datetime.now()
    format_date = date.strftime('%d') + '-' + date.strftime('%m') + '-' + date.strftime('%Y')
    wb = xlsxwriter.Workbook(f'./reports/{format_date}.xlsx')
    ws = wb.add_worksheet('Home')
    create_title(wb, ws)
    table_range = xl_range(4, 1, len(data)+5, 5)
    ws.add_table(table_range, {'data': data, 'columns':columns, 'name': 'relatorio', 'total_row': 1})
    wb.close()

