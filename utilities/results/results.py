#!/usr/bin/python
import json
import sqlite3


class Test:
    name = None
    data = []
    key = "START_TIME"

    def __init__(self, jsonEPTests):
        for key in jsonEPTests:
            self.name = key.upper()
            self.data = jsonEPTests[key]
            self.conn = sqlite3.connect('results.db')
            self.initTable()
            for item in self.data:
                TestItem(item, self.conn, self.name)

            self.conn.commit()
            self.conn.close()

    def initTable(self):
        tempdata = self.data[0]
        schemaHeader = "CREATE TABLE IF NOT EXISTS %s" % (self.name)
        schemaFields = self.buildSchemaString(tempdata)
        print "Opened database successfully";
        finalSQLCREATE = "%s\n %s;" % (schemaHeader, schemaFields)

        self.conn.execute(finalSQLCREATE)

        print "Table created successfully";

    def buildSchemaString(self, jsonTest):
        keys = ""
        for key in jsonTest:
            value = jsonTest[key]
            data_info = " "
            if key == self.key:
                data_info = key + " INT PRIMARY KEY NOT NULL"
                keys = "(" + data_info + ",\n" + keys
                continue
            elif type(value) is float:
                data_info += "REAL NOT NULL"
            elif type(value) is int:
                data_info += "INT NOT NULL"
            else:
                data_info += "TEXT NOT NULL"
            keys += key + data_info + ",\n"

        keys = keys[:-2] + "\n)"
        return keys


class TestItem:
    my_data = {}
    tableName = None

    def __init__(self, json_ep, conn, tableName):
        self.tableName = tableName
        self.my_data = json_ep
        self.add_to_database(conn)

    def add_to_database(self, conn):
        keys, values = self.buildKeysAndValues()
        try:
            conn.execute("INSERT OR IGNORE INTO %s (%s) VALUES (%s)" % (self.tableName, keys, values))
        except sqlite3.OperationalError, err:
            conn.execute("ALTER TABLE %s ADD COLUMN FAILURE TEXT;" % (self.tableName))
            conn.execute("INSERT OR IGNORE INTO %s (%s) VALUES (%s)" % (self.tableName, keys, values))
            print err


    @staticmethod
    def add_quotes(string):
        string = "'" + string + "'"
        return string

    def buildKeysAndValues(self):
        keys = ""
        values = ""
        for key in self.my_data:
            keys += key + ','
            val = self.my_data[key];
            if type(val) is int or type(val) is float:
                values += str(val) + ","
            else:
                values += self.add_quotes(val) + ","

        return keys[:-1], values[:-1]


json_data = ""
with open("data.txt") as json_file:
    json_data = json.load(json_file)

testsHolder = Test(json_data)
