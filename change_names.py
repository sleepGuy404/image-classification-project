# -*- coding: utf-8 -*-

import os
labels = []
with open("label_list.txt") as label_object:
    label_list = label_object.readlines()
    for str_label in label_list:
        temp_list = str_label.split(' ')
        labels.append(temp_list[0])

# 设定文件路径
for label in labels:
    path = 'classification/'+label
    i = 1
    # 对目录下的文件进行遍历
    for file in os.listdir(path):
        # 判断是否是文件
        if os.path.isfile(os.path.join(path, file)) == True:
            # 设置新文件名
            new_name = file.replace(file, f"{label}_used_for_classification_{i}.jpg")
            # 重命名
            os.rename(os.path.join(path, file), os.path.join(path, new_name))
            i += 1
# 结束
print("End")
