import os
from os import listdir
from os.path import isfile, join
databasename = "database_tab_delimited.txt"
index = 0
numberofnewlines = 0
newdatabase = ""
line = 0
mypath = os.getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for filename in onlyfiles:
	#printf "opening file: " + filename
	with open(filename, 'r+') as currfile:
		wholefile = currfile.read()
		newdatabase = wholefile
		while index < (len(newdatabase) - 10):
			#print "starting new loop"
			for i in xrange(len(newdatabase)):
				i = index
				index = index +1
				c = newdatabase[i]
				if c == '\n' or c == '\r':
					line = line + 1
					if i >= len(newdatabase) - 10:
						break
					htppstring = newdatabase [i +1] + newdatabase [i +2] + newdatabase [i +3] + newdatabase [i +4]
					#print "line: " + str(line) + " chars: " + newdatabase [i +1] + newdatabase [i +2] + newdatabase [i +3] + newdatabase [i +4]
					#print "http string: " + htppstring
					#if line == 129:
						#print c
					#	break
					if htppstring != "http":
						#print "line: " + str(line) + " chars: " + newdatabase [i +1] + newdatabase [i +3] + newdatabase [i +2] + newdatabase [i +4]
						#print "i =" + newdatabase[i]
						newdatabase = newdatabase[:i] + newdatabase[i + 1 : ]
						numberofnewlines = numberofnewlines + 1
						print "current line: " + str(line) + " current index: " + str(i) + "found newline to be replaced, total: " + str(numberofnewlines)
						break
			i = 0
			line = 0
		f2 = open("clean_" + filename, 'w')
		f2.write(newdatabase)
		f2.close()
#f2 = open("newdatabase_new.txt", "w")
#f2.write(newdatabase)
#f2.close()