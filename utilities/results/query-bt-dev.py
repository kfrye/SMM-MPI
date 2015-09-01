#!/bin/python3
import sqlite3
import sys
import statistics
from decimal import *

if len(sys.argv) != 3:
  print("Syntax is: query-bt-dev.py <# procs per node> <smi size>")
  exit(1)
procs = sys.argv[1]
smi = sys.argv[2]

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
    select_str = 'SELECT TIME_IN_SECONDS FROM bt WHERE PROCS_PER_NODE=' + procs + ' AND TOTAL_PROCESSES=' + str(p) + ' AND CLASS="' + c + '" AND VERIFICATION="SUCCESSFUL" AND SMI_SIZE=' + smi
    curs.execute(select_str)
    data = curs.fetchall()
    values = []
    for val in data:
      values.append(val[0])
    if len(data) > 2:
      print(round(statistics.stdev(values),2),end='\t')
print('\n')
conn.close()
