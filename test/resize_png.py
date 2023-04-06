# coding=utf-8

import re
from PIL import Image
import os, sys

if len(sys.argv) < 2:
	print("error")
	exit()

print(sys.argv)
dirr = sys.argv[1]

for fileName in os.listdir(dirr):
	filePath = dirr + fileName
	print(filePath)
	if '.png' in fileName and ('background' in fileName or 'front' in fileName):
		im = Image.open(filePath)# 打开一个jpg图像文件，注意路径要改成你自己的
		w, h = im.size# 获得图像尺寸:
		im.thumbnail((w//2, h//2))# 缩放到50%:
		document = open(filePath)
		if not os.path.exists('/Users/huanwenguo/Desktop/output/'):
			os.mkdir('/Users/huanwenguo/Desktop/output/')
		im.save('/Users/huanwenguo/Desktop/output/'+fileName, 'png')# 把缩放后的图像用jpeg格式保存:

