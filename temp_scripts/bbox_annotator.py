import json 


file_path = '/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/onehand10k/annotations/onehand10k_train.json'

json_file = json.load(open(file_path))


def calc_bbox(xs, ys, margin=0.3):

    #drop 0s from xs and ys
    # xs = [x for x in xs if x != 0]
    # ys = [y for y in ys if y != 0]

    xleft = min(xs)

    yleft = min(ys)

    # print(xleft, yleft)

    width = max(xs) - min(xs)

    height = max(ys) - min(ys)

    # print('x,y,w,h',xleft, yleft, width, height)

    
    xleft -= margin * width

    yleft -= margin * height

    width *= 1 + 2 * margin

    height *= 1 + 2 * margin


    # print('x,y,w,h',xleft, yleft, width, height)
    return xleft, yleft, width, height

def getXandY(keypoints):
    x_array = []
    y_array = []
    for i in range(0, len(keypoints), 3):
        if keypoints[i+2] != 0:
            x_array.append(keypoints[i])
            y_array.append(keypoints[i+1])
    return x_array, y_array

def getXandYNoFilter(keypoints):
    x_array = keypoints[::3]
    y_array = keypoints[1::3]
    return x_array, y_array

for i in range(len(json_file['annotations'])):
    keypoints = json_file['annotations'][i]['keypoints']
    x_array, y_array = getXandY(keypoints)
    x_arr, y_arr = getXandYNoFilter(keypoints)
    # print(x_array)
    # print(x_arr)
    # print()
    # print(y_array)
    # print(y_arr)
    (xleft, yleft, width, height) = calc_bbox(x_array, y_array)
    json_file['annotations'][i]['bbox'] = [xleft, yleft, width, height]
    # print()


# file_path = file_path.replace('.json', '_updatebbox.json')
print(file_path)
with open(file_path, 'w') as f:
    json.dump(json_file, f, indent=4)

