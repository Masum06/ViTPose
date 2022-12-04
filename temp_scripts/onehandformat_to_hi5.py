"""
Onehand10k Format:
wrist
thumb1-4
forefinger1-4
middle_finger1-4
ring_finger1-4
pinky_finger1-4

Hi5 Format:
wrist
indexA-D
middleA-D
ringA-D
pinkyA-D
thumbA-D
"""
import json
import cv2



def get_size(input):
    img = cv2.imread(input)
    height, width, channels = img.shape
    return height, width

def get_new_categories(old_categories):
    for category in old_categories:
        new = {}
        new['id'] = category['id']
        new['name'] = category['name']
        new['supercategory'] = category['supercategory']
        new['keypoints'] = [
                "wrist",
                "index_a",
                "index_b",
                "index_c",
                "index_d",
                "middle_a",
                "middle_b",
                "middle_c",
                "middle_d",
                "ring_a",
                "ring_b",
                "ring_c",
                "ring_d",
                "pinky_a",
                "pinky_b",
                "pinky_c",
                "pinky_d",
                "thumb_a",
                "thumb_b",
                "thumb_c",
                "thumb_d"
            ]
        new['skeleton'] = [
                [
                    1,
                    2
                ],
                [
                    1,
                    6
                ],
                [
                    1,
                    10
                ],
                [
                    1,
                    14
                ],
                [
                    1,
                    18
                ],
                [
                    2,
                    6
                ],
                [
                    6,
                    10
                ],
                [
                    10,
                    14
                ],
                [
                    2,
                    3
                ],
                [
                    3,
                    4
                ],
                [
                    4,
                    5
                ],
                [
                    6,
                    7
                ],
                [
                    7,
                    8
                ],
                [
                    8,
                    9
                ],
                [
                    10,
                    11
                ],
                [
                    11,
                    12
                ],
                [
                    12,
                    13
                ],
                [
                    14,
                    15
                ],
                [
                    15,
                    16
                ],
                [
                    16,
                    17
                ],
                [
                    18,
                    19
                ],
                [
                    19,
                    20
                ],
                [
                    20,
                    21
                ]
            ]
    return new
def get_new_keypoints(old_keypoints):
    """
    Onehand10k Format:
    wrist
    thumb1-4
    forefinger1-4
    middle_finger1-4
    ring_finger1-4
    pinky_finger1-4

    Hi5 Format:
    wrist
    indexA-D
    middleA-D
    ringA-D
    pinkyA-D
    thumbA-D
    """
    print()
    new_keypoints = []
    #add wrist
    new_keypoints.append(old_keypoints[0])
    new_keypoints.append(old_keypoints[1])
    new_keypoints.append(old_keypoints[2])

    thumb_keypoints = old_keypoints[3:(3+12)]
    forefinger_keypoints = old_keypoints[15:(15+12)]
    middle_finger_keypoints = old_keypoints[27:(27+12)]
    ring_finger_keypoints = old_keypoints[39:(39+12)]
    pinky_finger_keypoints = old_keypoints[51:(51+12)]
    new_keypoints.extend(forefinger_keypoints)
    new_keypoints.extend(middle_finger_keypoints)
    new_keypoints.extend(ring_finger_keypoints)
    new_keypoints.extend(pinky_finger_keypoints)
    new_keypoints.extend(thumb_keypoints)
    return new_keypoints

    


def get_new_annotations(old_annotations):
    new_annotations = []
    for annotation in old_annotations:
        new = {}
        new['id'] = annotation['id']
        new['image_id'] = annotation['image_id']
        new['category_id'] = annotation['category_id']
        new['iscrowd'] = annotation['iscrowd']
        new['area'] = annotation['area']
        new['bbox'] = annotation['bbox']
        new['segmentation'] = annotation['segmentation']
        new['keypoints'] = get_new_keypoints(annotation['keypoints'])
        new_annotations.append(new)
    return new_annotations

def onehand_to_hi5(onehand_path):
    print("Converting onehand10k to hi5 format")
    onehand = json.load(open(onehand_path))
    hi5_format = {}
    hi5_format['info'] = onehand['info']
    hi5_format['licenses'] = onehand['licenses']
    old_categories = onehand['categories']
    new_categories = []
    new_categories.append(get_new_categories(old_categories))
    hi5_format['categories'] = new_categories
    hi5_format['images'] = onehand['images']
    old_annotations = onehand['annotations']
    hi5_format['annotations'] = []
    new_annotations = []
    new_annotations.append(get_new_annotations(old_annotations))
    hi5_format['annotations'] = new_annotations
    return hi5_format

as_hi5 = onehand_to_hi5('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/onehand10k/onehand10k_train.json')

with open("/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/sample.json", "w") as outfile:
    json.dump(as_hi5, outfile, indent=4)

        
