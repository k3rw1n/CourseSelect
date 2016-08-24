#coding=utf-8
import csv
import itertools
import sys

reload(sys)
sys.setdefaultencoding('utf-8') 
csvfile = file('2.csv', 'rb')
reader = csv.reader(csvfile)
dictgrade = {}
dictmark = {}
dictname = {}
for line in reader:
    dictgrade[line[1]] = line[7]
    dictmark[line[1]] = line[-1]
    # dictname[line[1]] = line[0]

dictname['12003315']=u'高级经济学专题'
dictname['22003360']=u'中级计量经济学'
dictname['22003428']=u'中级宏观经济学'
dictname['22003429']=u'中级微观经济学'
dictname['21008300']=u'随机过程I'
dictname['21008305']=u'最优化方法I'
dictname['11009010']=u'中国马克思主义与当代'
dictname['21009306']=u'马克思主义与社会科学方法论'
dictname['11012002']=u'英语听说强化训练'
dictname['21012001']=u'综合英语'
dictname['24003378']=u'应用经济学研究方法论'
dictname['24003496']=u'产权经济学'
dictname['14003309']=u'社会保障理论与实践'
dictname['22003468']=u'金融理论与政策'
dictname['22003334']=u'中级运输经济学'
dictname['12003346']=u'微观金融理论'
dictname['22003494']=u'产业经济学英文文献阅读'


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
# sys.stdout = open('5star.txt','w')
fivestar =[]
for couses in queuelist:
	counter = 0
	for couse in couses:
		if dictmark[couse] == 'O':counter+=1
	if counter == 5:
		# print couses
		fivestar.append(couses)
# fivestar 是全部已经优先选择的课程 
allcourse=["12003315","22003360","22003428","22003429","21008300","21008305","11009010","21009306","11012002","21012001","24003378","24003496","14003309","22003468","22003334","12003346","22003494"]
lists = []
for ruler in range(9,13):
	
	star = []
	nostar = []
	for musthave in fivestar:
		grade = 0
		for course in musthave:
			grade += int(dictgrade[course])
		if grade == ruler:
			star.append(musthave)

	notin = [i for i in allcourse if i not in musthave] # 差集
	for i in itertools.combinations(notin, 2):
		list2 = list(i)
		if 15-ruler == int(dictgrade[list2[0]])+int(dictgrade[list2[1]]):
			nostar.append(list2)
	lists.append([star,nostar])


# 此时lists 格式为 lists = [[9分列表,6分列表],[10分列表,5分列表],[11分列表,4分列表],[12分列表,3分列表]]

comblist = []
for i in range(4):
    if lists[i][0] and lists[i][1]:
        for x in lists[i][0]:
            for y in lists[i][1]:
                comblist.append(x+y)

#comblist是所有分数为15分的合集



# for coursecomb in resultlist:
# 	for course in coursecomb:
# 		print dictname[course],
# 	print
sevenstar = []
for courses in comblist:
	counter = 0
	for course in courses:
		if dictmark[course] == 'O':
			counter+=1
	if counter == 7:
		sevenstar.append(courses)

# sevenstar 七星的满足要求的列表
for i in sevenstar[0]:
	print dictname[i]
