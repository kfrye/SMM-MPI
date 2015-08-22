import sqlite3
import sys
from decimal import *

if len(sys.argv) != 3:
  print("Syntax is: query-ep.py <# procs per node> <min/max>")
  exit(1)

procs = sys.argv[1]
func = sys.argv[2]

conn = sqlite3.connect('results.db')
classes = ["S", "W", "A", "B", "C"]
proc_1 = [1, 4, 9, 16]
proc_4 = [4, 9, 16, 25, 36, 49, 64] 
if procs == "1":
  processes = proc_1
else:
  processes = proc_4
 
curs = conn.cursor()

print('#\t', end="")
for c in classes:
  print(c, end="\t")

for p in processes:
  print(str('\n'+str(p)), end="\t")
  for c in classes:
    select_str = 'SELECT ' + func +  '(TIME_IN_SECONDS) FROM bt WHERE PROC_PER_NODE=' + procs + ' AND TOTAL_PROCESSES=' + str(p) + ' AND CLASS="' + c + '" AND VERIFICATION="SUCCESSFUL"'
    curs.execute(select_str)
    data = curs.fetchone()
    str_data = str(data[0])
    if str_data != 'None':
      num = float(str_data)
      print(round(num,2), end="\t") 
    else:
      print('\t', end="")
print('\n')
conn.close()
