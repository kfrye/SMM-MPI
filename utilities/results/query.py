__author__ = 'kmacarenco'
from prettytable import PrettyTable
import sqlite3

conn = sqlite3.connect('results.db')
curs = conn.cursor()
curs.execute('SELECT TIME_IN_SECONDS, CLASS, TOTAL_PROCESSES, VERIFICATION FROM EP')

col_names = [cn[0] for cn in curs.description]
rows = curs.fetchall()

y=PrettyTable()
y.padding_width = 1

x = 0
while x < len(col_names):
    y.add_column(col_names[x],[row[x] for row in rows])
    # y.align[col_names[x]]="l"
    # y.align[col_names[2]]="r"
    x +=1

print(y)
tabstring = y.get_string()

output=open("export.txt","w")
output.write("Population Data"+"\n")
output.write(tabstring)
output.close()

conn.close()
