import cv2
import os 
import json


annotation = json.load(open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/onehand10k/annotations/onehand10k_test.json'))

print(len(annotation['images']))

# image location: /home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/hi5_40k/test

#for image in folder

# for image in os.listdir('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/hi5_40k/train'):
#     try:
#         img = cv2.imread('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/hi5_40k/train/'+image)
#     except:
#         print(image)
    