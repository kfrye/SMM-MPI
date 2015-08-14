__author__ = 'kmacarenco'
import sqlite3

conn = sqlite3.connect('results.db')
cursor = conn.execute("""
          SELECT * from EP WHERE CPU_TIME=(
          SELECT MIN(CPU_TIME) from EP WHERE CLASS='S' AND TOTAL_PROCESSES=16)
          """)

for row in cursor:
    print row

cursor = conn.execute(""" SELECT CPU_TIME from EP WHERE CLASS='D' AND TOTAL_PROCESSES=4""")

for row in cursor:
    print row
