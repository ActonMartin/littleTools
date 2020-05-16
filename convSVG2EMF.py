import subprocess
import os

class convertSVGtoEMF(object):
    """
    代码的作用就是将文件夹下面的SVG图片转为EMF图片，方便插入到WORD中保持矢量。
    参数：
    inkscapePath:inkscapePath的安装的位置
    folder：您的SVg图片的父文件夹
    """
    def __init__(self, inkscapePath, folder):
        self.inkscapePath = inkscapePath
        self.folder = folder
    
    def startcovert(self):
        files = os.listdir(self.folder)
        count = 0
        for file in files:
            if file.endswith('.svg'):
                svg_path = self.folder + file
                emf_folder = self.folder + 'EMF/'
                emf_path = emf_folder + file.split('.')[0] + '.emf'
                print(emf_path,'开始进行转换')
                if not os.path.exists(emf_folder):
                    os.makedirs(emf_folder)
                count += 1
                cmd = "{0} -p {1} -o {2}".format(self.inkscapePath, svg_path, emf_path)
                process = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if count == len(files):
            print("所有的svg图像已经转换成功")


if __name__ == "__main__":
    inkscapePath = 'C:/Program Files/Inkscape/bin/inkscape.com'
    folder = 'E:/lll/'
    convertSVGtoEMF(inkscapePath, folder).startcovert()

    