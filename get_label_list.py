from os import listdir
import random


def get_item_labels(file):
    # 返回的是一个列表，获取文件夹里的文件名。
    filename_list = listdir(file)
    itemlabels_list = []
    for filename in filename_list:
        itemlabels_list.append(filename)
    return itemlabels_list


folder_names_dict = {'baihe':180,'dangshen':220, 'gouqi':185,
                'huaihua':179, 'jinyinhua':180}

# 读取所有的图片
total_lists = {}
for folder in folder_names_dict.keys():
    temp_list = get_item_labels(folder)
    random.shuffle(temp_list)
    total_lists[folder] = temp_list

# train_list.txt
# test_list.txt
# validate_list.txt


label = 0
with open('train_list.txt', 'w') as file_object_1:
    with open('test_list.txt', 'w') as file_object_2:
        with open('validate_list.txt', 'w') as file_object_3:
            for key, value in total_lists.items():
                num = 0
                for name in value:
                    num += 1
                    if num > folder_names_dict[key]:
                        file_object_1.write(key + "/" + name + ' ' + str(label) + '\n')
                    elif 140 < num <= folder_names_dict[key]:
                        file_object_2.write(key + "/" + name + ' ' + str(label) + '\n')
                    else:
                        file_object_3.write(key + "/" + name + ' ' + str(label) + '\n')
                label += 1
print('END')