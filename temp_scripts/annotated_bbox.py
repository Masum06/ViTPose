import cv2
import os
import json

image_path = '/home/hci-monster-linux/Documents/Hi5/data/coco/images/vid_2_sequence'

ann_json = {}
ann_json['info'] = {
    'description': 'Park Demo',
    'version': '1.0', #change this for each demo if we want to keep them organized
    'year': '2023',
    'date_created': '2023/1/26'
}

ann_json['licenses'] = ''
ann_json['images'] = []
ann_json['annotations'] = []



bbox_path = '/home/hci-monster-linux/Documents/Hi5/data/coco/images/vid_2_bbox.txt'
bboxes = []
with open(bbox_path) as f:
    for line in f:
        #example line: [[778, 289, 1128, 532]]
        line = line.replace('[','').replace(']','').replace(' ','')
        line = line.split(',')
        line = [int(x) for x in line]
        bboxes.append(line)


for filename in os.listdir(image_path):
    index = int(filename.replace('.jpg',''))
    file = os.path.join(image_path, filename)
    image = cv2.imread(file)
    height, width, _ = image.shape
    # print(height,width)
    #make the image dict for the image
    image_dict = {}
    image_dict['file_name'] = filename
    image_dict['height'] = height
    image_dict['width'] = width
    image_dict['id'] = int(filename.replace('.jpg',''))
    ann_json['images'].append(image_dict)

    #make the annotation dict for the image
    ann_dict = {}
    ann_dict['bbox'] = bboxes[index]
    ann_dict['keypoints'] = [0,0,1] *(21)
    ann_dict['category_id'] = 1
    ann_dict['id'] = int(filename.replace('.jpg',''))
    ann_dict['image_id'] = int(filename.replace('.jpg',''))
    segmentation = [[
                    85,
                    100,
                    85,
                    233.5,
                    85,
                    367,
                    192.5,
                    367,
                    300,
                    367,
                    300,
                    233.5,
                    300,
                    100,
                    192.5,
                    100
                ]]
    ann_dict['segmentation'] = segmentation
    ann_dict['is_crowd'] = 0
    ann_dict['area'] = height*width
    ann_json['annotations'].append(ann_dict)

    # print(json.dumps(ann_json, indent=4))
    # break

with open("/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/park_demo_vid/annotations/annotations_bboxes.json", "w") as outfile:
    json.dump(ann_json, outfile, indent=4)