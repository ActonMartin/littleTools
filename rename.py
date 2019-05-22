#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,shutil
#RED						完成--->>？？？
#后缀是BACK的是正面BACK-->FRONT
subfix="Second.SECOND_CAMERA_0.IMAGE_ID_RED.bmp"##文件后缀
dstfile_prefix='G:/file/201904012-20190418-工控机2/BACK/RED/'##某通道文件目的路径
cnt_start=1899
def process_files(path):
    cnt=cnt_start
    for root, dirs, files in os.walk(path):
           for name in files:
              if name.endswith(subfix):
                  srcfile=os.path.join(root, name)
                  print(cnt,name)
                  dstfile=dstfile_prefix+str(cnt)+".bmp"
                  shutil.copyfile(srcfile,dstfile)
                  #if cnt==1170:
                  #    print(srcfile)
                  cnt+=1




if __name__ == "__main__":
    path = 'F:/201904012-20190418-工控机2/'
    process_files(path)