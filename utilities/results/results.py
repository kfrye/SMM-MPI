#!/usr/bin/python
import json
import re
import sqlite3


class Test:
    def __init__(self):
        pass




#CREATE TABLE EP
#       (
#       "CPU_TIME          "REAL NOT NULL,
#       "MOP_S_TOTAL       "REAL NOT NULL,
#       "MOP_S_PROCESS     "REAL NOT NULL,
#       "TIME_IN_SECONDS   "REAL NOT NULL,
#
#       "COMPILED_PROCS    ",INT NOT NULL,
#       "ITERATIONS        ",INT NOT NULL,
#       "SIZE              ",INT NOT NULL,
#       "TOTAL_PROCESSES   ",INT NOT NULL
#       "EPOCH             ",INTEGER            PRIMARY KEY AUTOINCREMENT,
#
#       "FFLAGS            ",TEXT NOT NULL,
#       "COMPILE_DATE      ",TEXT NOT NULL,
#       "FLINK             ",TEXT NOT NULL,
#       "FLINKFLAGS        ",TEXT NOT NULL,
#       "FMPI_INC          ",TEXT NOT NULL,
#       "FMPI_LIB          ",TEXT NOT NULL,
#       "MPIF77            ",TEXT NOT NULL,
#       "N                 ",TEXT NOT NULL,
#       "NO_GAUSSIAN_PAIRS ",TEXT NOT NULL,
#       "OPERATION_TYPE    ",TEXT NOT NULL,
#       "RAND              ",TEXT NOT NULL,
#       "SUMS              ",TEXT NOT NULL,
#       "VERSION           ",TEXT NOT NULL,
#       "VERIFICATION      ",TEXT NOT NULL,
#       "CLASS             ",TEXT NOT NULL,
#
#       );

class ep(Test):
    name="EP"
    data = []
    reals=["CPU_TIME", "MOP_S_TOTAL", "MOP_S_PROCESS", "TIME_IN_SECONDS"]
    ints=["COMPILED_PROCS", "ITERATIONS", "SIZE", "TOTAL_PROCESSES", "EPOCH"]
    #Hardcoding is bad and will bite me in the but one day.
    not_text=["CPU_TIME","COMPILED_PROCS","ITERATIONS","MOP_S_TOTAL","MOP_S_PROCESS","SIZE","TIME_IN_SECONDS","TOTAL_PROCESSES"]
    def __init__(self, jsonEPTests):
        self.data = jsonEPTests 
        self.conn = sqlite3.connect('results.db')
        self.initTable()
        for item in  data:
            EpTest(item, self.conn)

        self.conn.commit()
        conn.close()

    def initTable():
        tempdata=data[0]
        schemaHeader="CREATE TABLE IF NOT EXISTS %s" % (self.name)
        schemaFields=buildSchemaString(tempdata)
        print "Opened database successfully";
        
        self.conn.execute("%s %s;" % (schemaHeader, schemaFields))

        print "Table created successfully";
    def buildSchemaString(jsonTest):
        keys = "("
        values = ""
        for key in self.my_data:
            data_info = " "            
            if key in self.reals:
                data_info += "REAL NOT NULL"            
            elif key in self.ints:
                data_info += "INT NOT NULL"            
            else:
                 data_info += "TEXT NOT NULL"            
            keys += key + data_info + ","
            
        keys += keys[:-1]+")"
        return keys
        
        


class EpTest:
    my_data={}
    #Hardcoding is bad and will bite me in the but one day.
    not_text=["CPU_TIME","COMPILED_PROCS","ITERATIONS","MOP_S_TOTAL","MOP_S_PROCESS","SIZE","TIME_IN_SECONDS","TOTAL_PROCESSES"]
    def __init__(self, json_ep, conn):
        self.my_data = json_ep
        self.add_to_database(conn)
    def add_to_database(self, conn):
        keys, values  = self.buildKeysAndValues()
        conn.execute("INSERT INTO EP (%s) VALUES (%s)" % (keys, values)
               )

    @staticmethod
    def add_quotes(string):
        string = "'" + string + "'"
        return string

    def buildKeysAndValues(self):
        keys = ""
        values = ""
        for key in self.my_data:
            keys+=key+','
            val = self.my_data[key];
            if key in self.not_text:
                values+=val+","
            else:
                values+=self.add_quotes(val)+","

        return keys[:-1], values[:-1]


json_data = ""
with open("data.txt") as json_file:
    json_data = json.load(json_file)

testsHolder = ep(json_data)

