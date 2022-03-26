import json
import xlsxwriter


def export_to_txt(matrix: list, path: str):
    if path[-4:] != '.txt':
        with open(path + '.txt', 'w', encoding='utf-8') as ef:
            ef.write(str(matrix))
    else:
        with open(path, 'w', encoding='utf-8') as ef:
            ef.write(str(matrix))


def export_to_json(matrix: list, path: str):
    json_matrix = {
        'matrix': matrix
    }
    if path[-5:] != '.json':
        with open(path + '.json', 'w', encoding='utf-8') as ef:
            json.dump(json_matrix, ef)
    else:
        with open(path, 'w', encoding='utf-8') as ef:
            json.dump(json_matrix, ef)


def format_csv(matrix: list, file):
    for row in range(len(matrix)):
        if row < 1:
            file.write('col{}'.format(row))
        else:
            file.write(',col{}'.format(row))
    for row, data in enumerate(matrix):
        file.write('\n')
        for i in range(len(data)):
            if i < 1:
                file.write(str(data[i]))
            else:
                file.write(',' + str(data[i]))


def export_to_csv(matrix: list, path: str):
    if path[-4:] != '.csv':
        with open(path + '.csv', 'w', encoding='utf-8') as ef:
            format_csv(matrix, ef)
    else:
        with open(path, 'w', encoding='utf-8') as ef:
            format_csv(matrix, ef)


def export_to_xlsx(matrix: list, path: str):
    if path[-5:] != '.xlsx':
        wb = xlsxwriter.Workbook(path + '.xlsx')
    else:
        wb = xlsxwriter.Workbook(path)
    ws = wb.add_worksheet()
    for row, data in enumerate(matrix):
        ws.write_row(row, 0, data)
    wb.close()
