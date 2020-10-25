import xlrd

from utils.search_data import SearchRegistrationData


class ExcelReader():

    @staticmethod
    def get_reg_data():
        """Getting data for registration"""

        wb = xlrd.open_workbook(r"./test_data.xlsx")
        sheet = wb.sheet_by_index(0)
        reg_data = []

        for i in range(1, sheet.nrows):
            for j in range(0, sheet.ncols - 12):
                data_row = SearchRegistrationData(sheet.cell(i, j).value, sheet.cell(i, j + 1).value,
                                                     sheet.cell(i, j + 2).value, sheet.cell(i, j + 3).value,
                                                     sheet.cell(i, j + 4).value, sheet.cell(i, j + 5).value,
                                                     sheet.cell(i, j + 6).value, sheet.cell(i, j + 7).value,
                                                     sheet.cell(i, j + 8).value, sheet.cell(i, j + 9).value,
                                                     sheet.cell(i, j + 10).value, sheet.cell(i, j + 11).value,
                                                     sheet.cell(i, j + 12).value)
                reg_data.append(data_row)

        return reg_data


# a = ExcelReader()
# reg_data = a.get_reg_data()
# print(reg_data[0].fname)