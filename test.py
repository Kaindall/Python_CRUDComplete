cols = ("Cname", "Csurname", "Expenses", "Gender", "Nationality")

data = (("Jacki","Enders",4482,"Female","Panamanian"),
("Allegra","Ucchino",9814,"Female","Eskimo"),
("Barbabas","Collingham",5933,"Male","Panamanian"))

       
for row in data:
       for e, element in enumerate(row):
              if type(element) == str:
                     print (f'{cols[e]} = "{element}"')
              else:
                     print (f'{cols[e]} = {element}')
       