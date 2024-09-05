import openpyxl

def get_list_from_excel():
    creds= openpyxl.load_workbook()
    login_creds = creds["login_creds"]
    credentials =[]
    for row in range(1,9):
        nested_creds =[]
        for column in range(1,3):
            data = login_creds.cell(row,column)
            nested_creds.append(data.value)
        credentials.append(nested_creds)

    return credentials