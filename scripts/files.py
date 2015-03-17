import os

train = open("../data/train.txt","w")
test = open("../data/test.txt","w")
llist = list(open("../label.txt"))

"""
for idx in range(0,30000):
	for dup in range(0,11):
		fName = "%d_00_%04d.bmp" % (idx,dup)
                label = llist[idx].split()[0]
		txtIn = "%s %s\n" % (fName, label)
		train.write(txtIn)
		os.system("mv ../data/%s ../data/train/%s" % (fName, fName))
"""
for idx in range(30000,42000):
	for dup in range(0,11):
		fName = "%d_00_%04d.bmp" % (idx,dup)
                label = llist[idx].split()[0]
		txtIn = "%s %s\n" % (fName, label)
		test.write(txtIn)
		os.system("mv ../data/%s ../data/test/%s" % (fName, fName))
train.close()
test.close()
