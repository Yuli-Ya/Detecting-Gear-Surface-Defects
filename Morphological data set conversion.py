import imageprocess
import cv2
import numpy as np 
import os
rootdir = '4'#需要修改的图片路径
m = 1

def imagepro(image):
	image = cv2.imread(image,cv2.IMREAD_UNCHANGED)
	image = cv2.resize(image,(416,416))
	#将灰度图像转换为三通道灰度图像（三通道各点像素值相同，便于训练） 
	image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	image = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR) 
	#进行两次滤波  模糊背景干扰
	image = cv2.medianBlur(image,3)                          #中值滤波操作 
	image = cv2.GaussianBlur(image,(3,3),0)                  #高斯滤波操作
	return image

list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
	path = os.path.join(rootdir,list[i])
	if os.path.isfile(path):  #每张图片转换为四种形态学图像，并分别保存
		r = imageprocess.imagepro(path)
		cv2.imwrite('test1\\4\\impro'+str(m)+'.jpg',r)
		m = m+1
	

