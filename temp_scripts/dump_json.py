import json

train_file = json.load(open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/hi5_40k/annotations/person_keypoints_train.json'))
test_file = json.load(open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/hi5_40k/annotations/person_keypoints_test.json'))
val_file = json.load(open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/data/hi5_40k/annotations/person_keypoints_valid.json'))

#write json file
with open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/ViTPose/data/hi5_40k/hi5_40k_train.json', 'w') as f:
    json.dump(train_file, f, indent=4)


with open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/ViTPose/data/hi5_40k/hi5_40k_test.json', 'w') as f:
    json.dump(test_file, f, indent=4)

with open('/home/hci-monster-linux/Documents/Hi5/alex_folder/Hi5-data/ViTPose/data/hi5_40k/hi5_40k_valid.json', 'w') as f:
    json.dump(val_file, f, indent=4)
