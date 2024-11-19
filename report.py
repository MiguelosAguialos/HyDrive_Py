import xlsxwriter
from xlsxwriter.utility import xl_range
import datetime
from common_codes import create_folder

def create_title(wb, ws):
    title_format = wb.add_format({'bold': True})
    title_format.set_size(16)
    title_format.set_align('center')
    title_format.set_valign('vcenter')
    title_format.set_font_color('#2C6FC3')
    ws.merge_range('C2:H4', 'HyDrive - Monitoring System', title_format)
    date = datetime.datetime.now()
    format_date = date.strftime('%d') + '/' + date.strftime('%m') + '/' + date.strftime('%Y')
    ws.write('I2', 'Classificação: Restrito', wb.add_format({'bold': True}))
    ws.write('I3', f'Última atualização: {format_date}', wb.add_format({'bold': True}))
    ws.write('I4', 'Versão: 1.0', wb.add_format({'bold': True}))
    ws.merge_range('B2:B4', '', title_format)
    ws.embed_image('B2', './images/report_icon.png', options={'x_scale': 0.1, 'y_scale': 0.1})

def generate_report(data):
    create_folder('./reports')
    wb = xlsxwriter.Workbook('./reports/demo.xlsx')
    ws = wb.add_worksheet('Home')
    create_title(wb, ws)
    wb.close()

