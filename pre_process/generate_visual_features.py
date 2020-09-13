
import os
import csv
import torch
import torch.nn as nn
from torchvision import models, transforms
from torch.autograd import Variable
import numpy as np
from PIL import Image
import warnings
from tqdm import tqdm

warnings.filterwarnings("ignore")

target_path = './amazon-product-reviews_sport-and-outdoors_IMG/sports_and_outdoors/files/'
target_img = os.listdir(target_path)

img_path_list = []
with open('./prod_stats_del.tsv') as f:
    tsvreader = csv.reader(f, delimiter='\t')
    for line in tsvreader:
    	product_id = target_path + line[0]
    	img_path = product_id + '/' + line[0] + '_' + 'imUrl.jpg'
    	L_image=Image.open(img_path)
    	out = L_image.convert("RGB")
    	out.save(img_path)
    	img_path_list.append(img_path)


# img_path_list = []
# for i in target_img:
#   img_path = target_path + '/' + i
#   img = img_path + '/' + i + '_' + 'imUrl.jpg'
#   img_path_list.append(img)


transform1 = transforms.Compose([
    transforms.Scale(256),
    transforms.CenterCrop(224),
    transforms.ToTensor()]
)

res = np.zeros(shape=(17325,2048))
for idx, i in enumerate(tqdm(img_path_list)):
	img = Image.open(i)
	img1 = transform1(img)

	# print(img1.size())

	resnet50_feature_extractor = models.resnet50(pretrained = True)
	resnet50_feature_extractor.fc = nn.Linear(2048, 2048)
	torch.nn.init.eye(resnet50_feature_extractor.fc.weight)

	for param in resnet50_feature_extractor.parameters():
	    param.requires_grad = False

	x = Variable(torch.unsqueeze(img1, dim=0).float(), requires_grad=False)

	# print(x)
	y = resnet50_feature_extractor(x)
	y = y.data.numpy()
	res[idx] = y
	
print(res)
np.save("vis_info.npy", res)
# np.savetxt(feature_path, y, delimiter=',')
# y_ = np.loadtxt(feature_path, delimiter=',').reshape(1, 2048)

# print(y_)