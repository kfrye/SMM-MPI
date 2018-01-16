#!/usr/bin/python
import json


class Tests(object):
    def __init__(self, tests, name):
        self.tests = tests
        self.name = name
        self.export_tests()

    def export_tests(self):
        with open(self.name + ".ptdf", "w+") as ptdf_file:
            ptdf_file.write("Application " + self.name + '\n')
            ptdf_file.write('Resource "wyeast cluster" grid|machine\n')
            ptdf_file.write('Resource "v3.3.1" build\n')
            ptdf_file.write('Resource "Linux version 3.17.4-301.fc21.x86_64" environment\n')
            ptdf_file.write('Resource "self generated" dataFiles\n')
            ptdf_file.write('Resource "whole time" time\n')
            ptdf_file.write('Resource ext4 fileSystem\n')
            ptdf_file.write('Resource "self instrumentation" perfToolName\n')
            ptdf_file.write('Resource "time in seconds" metric\n')
            for test_dictionary in self.tests:
                execution = self.name.lower() + '-' + str(test_dictionary['START_TIME'])
                ptdf_file.write("Execution " + execution + ' ' + self.name + '\n')
                for key in test_dictionary:
                    if key != 'TIME_IN_SECONDS':
                        ptdf_file.write("ResourceAttribute " + execution + ' ' +
                                        key.lower() + ' "' + str(test_dictionary[key]) + '" string\n')
                ptdf_file.write('PerfResult ' + execution +
                                ' "wyeast cluster,v3.3.1,Linux version 3.17.4-301.fc21.x86_64,self generated,' +
                                execution + ',whole time,ext4" "self instrumentation" "time in seconds" ' +
                                str(test_dictionary['TIME_IN_SECONDS']) + ' s ' +
                                str(test_dictionary['START_TIME']) + ' noValue\n')


class Matrix:
    def __init__(self, tests):
        self.all_data = tests
        self.process_matrix()

    def process_matrix(self):
        for test_type in self.all_data:
            test_name = test_type.upper()
            data = self.all_data[test_type]
            Tests(data, test_name)


with open("data.txt") as json_file:
    json_data = json.load(json_file)
    Matrix(json_data)
