# Detecting-Gear-Surface-Defects
If you use this code ,Please conference "Detecting Gear Surface Defects Using Background-weakening Method and Convolutional Neural Network"
1. Experiment preparation：
	Resize the four types of images into 416*416；
	The data image is filtered twice according to the algorithm given in the paper；
	Label is obtained by labeling images with labelimage；
	Download the YOLOv3 project
git clone https://github.com/pjreddie/darknet  
cd darknet  
Prepare the training data set
According to the following folder structure, put the training data set under each folder, generate 4 training, test and verify TXT file list
VOCdevkit 
—VOC2007 
——Annotations 
——ImageSets 
———Layout 
———Main 
———Segmentation 
——JPEGImages 
In Annotations are all the XML files 
JPEGImages are all training images 
In Main, there are 4 TXT files, among which test.txt is the test set, train.txt is the training set, val. TXT is the verification set, and trainval. TXT is the training and verification set.
Download the voc_label.py file to the VOCdevkit sibling path to generate a list of training and validation files
wget https://pjreddie.com/media/files/voc_label.py
Modify sets to the name of the training sample set
sets=[('2007', 'train')]
Modify the class label for classes as a training sample set
classes=[str(i) for i in range(10)]
Download pre-trained weights on Imagenet
wget https://pjreddie.com/media/files/darknet53.conv.74
Modify the cfg/voc.data
classes= 4  #classes is the total number of categories in the training sample set
train  = /home/user/darknet/2007_train.txt  #train is the path where the training sample set is located
valid  = /home/user/darknet/2007_val.txt  #valid path is the path to verify the sample set
names = data/voc.names  
backup = backup
Create a new folder backup under the darknet folder
Modify data/voc.name to be the tag name of the sample set
break，lack，scratch，normal
Modify the filters = 3*(class+4+1) in cfg/yolov3-voc.cfg

2 Yolo training
Use kmeans algorithm to set K=9 to find 9 suitable auchor；
Find the darknet/cfg/yolov3.cfg file and change the auchor in it to the optimal auchor obtained by kmeans；
Return to the darknet root for model training
Start training
./darknet detector train cfg/voc.data cfg/yolov3-voc.cfg darknet53.conv.74 -gpus 0,1
Detect
./darknet detect cfg/yolov3-voc.cfg weights/yolov3.weights 
