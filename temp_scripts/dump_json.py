import json

train_file = json.load(open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/hi5_50K/50K_Dataset/data/annotations/person_keypoints_train41k.json'))
test_file = json.load(open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/hi5_50K/50K_Dataset/data/annotations/person_keypoints_test6k.json'))
val_file = json.load(open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/hi5_50K/50K_Dataset/data/annotations/person_keypoints_valid10k.json'))

#write json file
with open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/ViTPose/data/hi550k/annotations/hi550k_train41k.json', 'w') as f:
    json.dump(train_file, f, indent=4)


with open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/ViTPose/data/hi550k/annotations/hi550k_test6k.json', 'w') as f:
    json.dump(test_file, f, indent=4)

with open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/ViTPose/data/hi550k/annotations/hi550k_val10k.json', 'w') as f:
    json.dump(val_file, f, indent=4)
