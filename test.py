cols = ("idClient", "Cname", "Csurname", "Expenses", "Gender", "Nationality")

data = ((2, "Jacki","Enders",4482,"Female","Panamanian"),
(3, "Allegra","Ucchino",9814,"Female","Eskimo"),
(4, "Barbabas","Collingham",5933,"Male","Panamanian"))

table = "client"       


def quickfunc (cols, data):
       for row in data:
              line = ""
              
              for e, element in enumerate(row):
                     if type(element) == str:
                            if len(line) == 0:
                                   line = line + (f'{cols[e]} = "{element}"')
                            else:
                                   line = line + (f', {cols[e]} = "{element}"')
                     else:
                            if len(line) == 0:
                                   line = line + (f'{cols[e]} = {element}')
                            else:
                                   line = line + (f', {cols[e]} = {element}')
              return line

def quickfunc2 (cols, data):
       print(f'''
              INSERT INTO {table}({cols})\n
              VALUES {data}
              ON DUPLICATE KEY UPDATE
              
              ''')
              
              
quickfunc2 (cols, data)
       