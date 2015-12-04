#!/usr/local/bin/python3
import sqlite3
import json
import sys
from decimal import *

if len(sys.argv) != 6:
  print("Syntax is: query.py <test type> <# procs per node> <min/max> <smi size> <ht on/off>")
  exit(1)

test = sys.argv[1]
procs = sys.argv[2]
func = sys.argv[3]
smi = sys.argv[4]
hts = sys.argv[5]

if hts == "on":
  ht = "1"
elif hts == "off":
  ht = "0"
else:
  print("ht must be set to 'on' or 'off'")
  exit(1)

if test not in ["ep", "bt", "ft", "lu", "sp", "mg"]:
  print("The test type must be 'ep', 'bt', 'ft', 'lu', 'sp', or 'mg'")
  exit(1)

conn = sqlite3.connect('results.db')
classes = ["S", "W", "A", "B", "C"]

if test != "bt" and test != "sp":
  proc_1 = [1, 2, 4, 8, 16]
  proc_4 = [4, 8, 16, 32, 64]
else:
  proc_1 = [1, 4, 16]
  proc_4 = [4, 16, 64]
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
    curs.execute('SELECT ' + func + '(TIME_IN_SECONDS) FROM ' + test + ' WHERE PROCS_PER_NODE=' + procs + ' AND TOTAL_PROCESSES=' + str(p) + ' AND CLASS="' + c + '" AND VERIFICATION="SUCCESSFUL" AND SMI_SIZE=' + smi + ' AND HT=' + ht)
    data = curs.fetchone()
    str_data = str(data[0])
    if str_data != 'None':
      num = float(str_data)
      print(round(num,2), end="\t") 
print('\n')
conn.close()
