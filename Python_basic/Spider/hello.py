import os


import os
 
current_work_dir = os.path.dirname(__file__)  # 当前文件所在的目录

weight_path = "\jinjiang.txt"
 
#weight_path = os.path.join(current_work_dir, weight_path)  # 再加上它的相对路径，这样可以动态生成绝对路径

print(current_work_dir + weight_path)



