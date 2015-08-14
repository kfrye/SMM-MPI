#!/usr/bin/python
import json
import re
import sqlite3


class TriesArr(list):
    min = ""
    max = ""
    avg = ""
    median = ""



class Test:
    def __init__(self):
        pass


class TestFactory:
    result = {}

    def __init__(self, json_ep_tests, conn):
        for size in json_ep_tests:
            size_dict = json_ep_tests[size]
            t = TriesArr()
            for aTry in size_dict:
                t.append(EpTest(size_dict[aTry], conn))
            self.result[size] = t


class TestsDict(dict):
    def __init__(self, json_ep_tests, conn):
        for key in json_ep_tests:
            self[key] = TestFactory(json_ep_tests[key], conn).result
        pass


class ep(Test):
    def __init__(self, jsonEPTests):

        conn = sqlite3.connect('results.db')
        self.tests = TestsDict(jsonEPTests['ep'],conn)
        conn.commit()
        conn.close()


class EpTest:
    my_data={}
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

conn = sqlite3.connect('results.db')

print "Opened database successfully";

conn.execute('''CREATE TABLE IF NOT EXISTS EP
       (
       ID INTEGER PRIMARY KEY AUTOINCREMENT,
       CPU_TIME          REAL NOT NULL,
       COMPILE_DATE      TEXT NOT NULL,
       COMPILED_PROCS    INT NOT NULL,
       FFLAGS            TEXT NOT NULL,
       FLINK             TEXT NOT NULL,
       FLINKFLAGS        TEXT NOT NULL,
       FMPI_INC          TEXT NOT NULL,
       FMPI_LIB          TEXT NOT NULL,
       ITERATIONS        INT NOT NULL,
       MPIF77            TEXT NOT NULL,
       MOP_S_TOTAL       REAL NOT NULL,
       MOP_S_PROCESS     REAL NOT NULL,
       N                 TEXT NOT NULL,
       NO_GAUSSIAN_PAIRS TEXT NOT NULL,
       OPERATION_TYPE    TEXT NOT NULL,
       RAND              TEXT NOT NULL,
       SIZE              INT NOT NULL,
       SUMS              TEXT NOT NULL,
       TIME_IN_SECONDS   REAL NOT NULL,
       VERSION           TEXT NOT NULL,
       CLASS             CHAR(1) NOT NULL,
       VERIFICATION      TEXT NOT NULL,
       TOTAL_PROCESSES   INT NOT NULL
       );''')

print "Table created successfully";
conn.close()

testsHolder = ep(json_data)

