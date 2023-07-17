import cv2
import os 
import json
import sys
import time

# take input from cmd argument
train_test = str(sys.argv[1]).strip() # train or test

# can you copy and paste the path to the dataset here ?
data_root = 'F:/Hand_Dataset/final_split_5_19'
train_root ='F:/Hand_Dataset/final_split_5_19/' + train_test

ann_file = f'{data_root}/annotations/hi5_500k_{train_test}.json'
new_ann_file = f'{data_root}/annotations/hi5_500k_{train_test}_uncorrupted.json'

# this should work gonna disconnect my wifi is trash
# Let's also load the JSON file here and export a new JSON with the corrupted images removed
with open(ann_file) as f:
    ann = json.load(f)

# Let's iterate through the JSON file instead of the directory

images = ann['images']
annotations = ann['annotations']

corrupted_images = []
num = 0
start_time = time.time()
for image in images:
    file = image['file_name']
    num += 1
    time_now = time.time()
    try:
        img = cv2.imread(os.path.join(train_root, file))
        print("\r", file, int(10000*num/len(images))/100, "\% finished. Elapsed time: ", int(time_now - start_time), "s", end="")
    except:
        print(file)
        image_id = image['id']
        corrupted_images.append(image_id)

new_json = {}
new_annotations = []
new_images = []

for annotation in annotations:
    if annotation['image_id'] not in corrupted_images:
        new_annotations['annotations'].append(annotation)

for image in ann['images']:
    if image['id'] not in corrupted_images:
        new_images['images'].append(image)

new_json['images'] = new_images
new_json['annotations'] = new_annotations

with open(new_ann_file, 'w') as f:
    json.dump(new_json, f)

## Print numbeer of corrupted and total images
print("Number of corrupted images: ", len(corrupted_images))
print("Total number of images: ", len(images))