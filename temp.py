from os import listdir
import random


def get_item_labels(file):
    # 返回的是一个列表，获取文件夹里的文件名。
    filename_list = listdir(file)
    itemlabels_list = []
    for filename in filename_list:
        itemlabels_list.append(filename)
    return itemlabels_list


folder_names = ['baihe','dangshen', 'gouqi',
                'huaihua', 'jinyinhua']

# 读取所有的图片
total_lists = {}
for folder in folder_names:
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
                    if num <= 120:
                        file_object_1.write(key + "/" + name + ' ' + str(label) + '\n')
                    if 120 < num <= 150:
                        file_object_2.write(key + "/" + name + ' ' + str(label) + '\n')
                    if num > 150:
                        file_object_3.write(key + "/" + name + ' ' + str(label) + '\n')
                label += 1
