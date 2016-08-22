# -*- coding: cp936 -*-
import csv
import itertools
import sys

csvfile = file('2.csv','rb')
reader = csv.reader(csvfile)
dictgrade = {}
dictmark = {}
for line in reader:
	dictgrade[line[1]]=line[7]
	dictmark[line[1]]=line[-1]
# print dictgrade
queuelist=[]
for i in itertools.combinations(("12003315","22003360","22003428","22003429","21008300","21008305"), 2):
	for x in ("11009010","21009306","11012002","21012001"):
		for y in ("24003378","24003496","14003309","22003468"):
			for z in ("22003334","12003346","22003494"):
				tmp = list(i)
				tmp.append(x)
				tmp.append(y)
				tmp.append(z)
				queuelist.append(tmp)
sys.stdout = open('5star.txt','w')
fivestar =[]
for couses in queuelist:
	counter = 0
	for couse in couses:
		if dictmark[couse] == 'O':counter+=1
	if counter == 5:
		print couses
		fivestar.append(couses)

allcourse=["12003315","22003360","22003428","22003429","21008300","21008305","11009010","21009306","11012002","21012001","24003378","24003496","14003309","22003468","22003334","12003346","22003494"]
for ruler in range(9,13):
	sys.stdout = open('%s.txt'%ruler,'w')
	for musthave in fivestar:
		grade = 0
		for course in musthave:
			grade += int(dictgrade[course])
		if grade == ruler:print "%s,grade= %d" %(musthave,grade)

	sys.stdout = open('%smatch.txt'%ruler,'w')
	for i in itertools.combinations(allcourse, 2):
		list2 = list(i)
		if 15-ruler == int(dictgrade[list2[0]])+int(dictgrade[list2[1]]):print list2,'grade = ',int(dictgrade[list2[0]])+int(dictgrade[list2[1]])