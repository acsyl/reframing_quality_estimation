import os, numpy as np, pickle
import csv
import random

dic_same = pickle.load(open('same_cat.pickle', 'rb'))


dic2 = pickle.load(open('2_cat.pickle', 'rb'))
dic3 = pickle.load(open('3_cat.pickle', 'rb'))
dic4 = pickle.load(open('4_cat.pickle', 'rb'))
dic5 = pickle.load(open('5_cat.pickle', 'rb'))

all_review = pickle.load(open('review.pickle', 'rb'))

rand_pic = {}
with open('prod_stats_del.tsv') as f:
	tsvreader = csv.reader(f, delimiter='\t')
	for line in tsvreader:
		# print(line[0])
		product_id = './files/' + line[0]
		categories_id = product_id +  "/" + line[0] + "_" + "categories.en"
		with open(categories_id) as f1:
			tmp = []
			tsvreader1 = csv.reader(f1, delimiter='\t')
			for line1 in tsvreader1:
				tmp.append(line1[0])
			k = ""
			for i in tmp:
				k += "+" + i
			s = dic_same[k]
			if(len(tmp) >= 5):
				key = tmp[0] + '+' + tmp[1] + '+' + tmp[2] + '+' + tmp[3] + '+' + tmp[4]
				v = dic5[key]
				res = [item for item in v if item not in s]
				if len(res) > 0:
					rand_pic[line[0]] = [res[0]]
			if(len(tmp) >= 4):
				key = tmp[0] + '+' + tmp[1] + '+' + tmp[2] + '+' + tmp[3] 
				v = dic4[key]
				res = [item for item in v if item not in s]
				while(len(res) > 0):
					if line[0] in rand_pic:
						if(rand_pic[line[0]][0]!= res[0]):
							rand_pic[line[0]].append(res[0])
							break
						else:
							res = res[1:]
					else:
						rand_pic[line[0]] = [res[0]]
						break
			if(len(tmp) >= 3):
				key = tmp[0] + '+' + tmp[1] + '+' + tmp[2] 
				v = dic3[key]
				res = [item for item in v if item not in s]
				while(len(res) > 0):
					if line[0] in rand_pic:
						if(rand_pic[line[0]][0]!= res[0]):
							rand_pic[line[0]].append(res[0])
							break
						else:
							res = res[1:]
					else:
						rand_pic[line[0]] = [res[0]]
						break 
			if(len(tmp) >= 2):
				key = tmp[0] + '+' + tmp[1] 
				v = dic2[key]
				res = [item for item in v if item not in s]
				while(len(res) > 0):
					if line[0] in rand_pic:
						if(rand_pic[line[0]][0]!= res[0]):
							rand_pic[line[0]].append(res[0])
							break
						else:
							res = res[1:]
					else:
						rand_pic[line[0]] = [res[0]]
						break
			if ((line[0] not in rand_pic) or len(rand_pic[line[0]]) < 4):
				if line[0] in rand_pic:
					pic = set(rand_pic[line[0]])
					while(len(pic)< 4):
						c = random.choice(all_review)
						if(c not in s):
							pic.add(c)
					rand_pic[line[0]] = list(pic)
				else:
					c = random.choice(all_review)
					rand_pic[line[0]] = set()
					while(len(rand_pic[line[0]])< 4):
						c = random.choice(all_review)
						if(c not in s):
							rand_pic[line[0]].add(c)
					rand_pic[line[0]] = list(rand_pic[line[0]])

with open('rand_pic.pickle', 'wb') as handle:
    pickle.dump(rand_pic, handle, protocol=pickle.HIGHEST_PROTOCOL)





