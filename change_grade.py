#!/usr/bin/env python

import re


def changeStudentGrade(studentName, studentGrade ):
#Scan through lines of data in a file.  If the student's name is found in the file then replace their grade with the given grade.

	for line in fileinput.input('-'):
    	    m = re.search(studentName, line)
    	    values = line.rstrip().split(',') #note that split accepts an optional parameter to define what character the string is split on. If none is provided it defaults to any whitespace character
    	    if m:
        	    values[3] = studentGrade
    	    print ",".join(values)


if __name__=="__main__":
	from sys import stderr,stdout,argv,exit	
	if len(argv) != 3:
		stderr.write("Usage: change_grade.py STRING  NUMBER\n")
		exit(1)

	changeStudentGrade(argv[1], argv[2])

