#!/usr/bin/python
__author__ = 'kmacarenco'
from prettytable import PrettyTable
import sqlite3
import json

classes = ["S", "W", "A", "B", "C", "D", "E"]
tests = ["ep", "bt" ,"ft"]
ppn = [1,4]
proc_1 = [1, 2, 4, 8, 16]
proc_4 = [4, 8, 16, 32, 64]

conn = sqlite3.connect('results.db')
curs = conn.cursor()
res = {}
for b in tests:
    res[b]={}
    for p in ppn:
        res[b][p]={}
        for c in classes:
            curs.execute('SELECT TOTAL_PROCESSES, MIN(TIME_IN_SECONDS) FROM '+ b + ' WHERE PROCS_PER_NODE = '+ str(p) +' AND SMI_SIZE = 0 AND CLASS="'+c+'" AND (TOTAL_PROCESSES=1 OR TOTAL_PROCESSES=2 OR TOTAL_PROCESSES=4 OR TOTAL_PROCESSES=8 OR TOTAL_PROCESSES=16 OR TOTAL_PROCESSES=32 OR TOTAL_PROCESSES=64) GROUP BY TOTAL_PROCESSES, CLASS ORDER BY TOTAL_PROCESSES')
            col_names = [cn[0] for cn in curs.description]
            rows = curs.fetchall()


            data = []
            for x in rows:
            #    print x[0]
                data.append({x[0]:x[1]})

            #print data
            if len(data) > 0:
                res[b][p][c]=data
            #json_data = json.dumps(data)
            #print json_data
conn.close()

with open('graphReady', 'w') as outfile:
  json.dump(res, outfile, sort_keys=True, indent=4, separators=(',', ': '))

