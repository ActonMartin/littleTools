# -*- coding: utf-8 -*-
import os
import shutil

#起始目录
path = 'G:/file/201904012-20190418-GKJ2/BACK/zz22'
#临时目录
folderPath = 'G:/file/201904012-20190418-GKJ2/BACK/ZZZZZZZZ'
#give the img list
file_list = sorted(os.listdir(path))
files_each_folder=1000           #设置每个文件夹里面的文件数目
folder_number = int((len(file_list)+files_each_folder-1)/files_each_folder)   #文件夹数目向上取整
sort_folder_number = [x for x in range(0,folder_number)]

prefix_folder_front_Center='IMAGE_PATCH_FRONT_Center_PART'   #正面中心前缀
prefix_folder_front_Up_Down='IMAGE_PATCH_FRONT_Up_Down_PART'   #正面上下边前缀
prefix_folder_front_Light_Right='IMAGE_PATCH_FRONT_Light_Right_PART'   #正面左右边前缀

prefix_folder_back_Center='IMAGE_PATCH_BACK_Center_PART'   #反面中心前缀
prefix_folder_back_Up_Down='IMAGE_PATCH_BACK_Up_Down_PART'   #正面上下边前缀
prefix_folder_back_Light_Right='IMAGE_PATCH_BACK_Light_Right_PART'   #正面左右边前缀


# 创建文件夹
for number in sort_folder_number:
    new_folder_path = os.path.join(folderPath,prefix_folder_back_Center+'%s'%number)#new_folder_path is ‘folderPath\prefix_folder_back+number'

    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print("new a floder named "+str(number)+'at the path of '+ new_folder_path)
'''define the first foloderNumber_index'''
folderNumber_index = 0
print('there are '+str(len(file_list))+' files at the path of '+path)
for index,j in enumerate(file_list):
    #for i in range(0,len(file_list)):
    old_file_path = os.path.join(path,j)
    '''define the number,it decides how many imgs each folder process'''
    #number = 1000 #int(len(file_list)/folder_number)
    if(index%files_each_folder ==0 and index!=0):
        folderNumber_index +=1
    new_file_path = os.path.join(folderPath,prefix_folder_back_Center+'%s'%(folderNumber_index))
    if not os.path.exists(new_file_path):
        print('not exist path:'+new_file_path)
        break
    shutil.copy(old_file_path,new_file_path)
    print('success copy file from '+ old_file_path +' to '+new_file_path)
    #shutil.make_archive(new_file_path,'zip',new_file_path)
   
for p in range(folder_number):
    exist_folder = os.path.join(folderPath,prefix_folder_back_Center+'%s'%p)
    shutil.make_archive(exist_folder,'zip',exist_folder)
    print('success make compress  of the '+ exist_folder )
  
    
 


