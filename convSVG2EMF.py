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
        for file in files:
            count = 0
            svg_list = []
            if file.endswith('.svg'):
                svg_list.append(file)
                svg_path = self.folder + file
                emf_path = self.folder + 'EMF/' + file.split('.')[0] + '.emf' 
                subprocess.run([self.inkscapePath, svg_path, '-M', emf_path])
                count += 1
            if count == len(svg_list):
                print("所有的svg图像已经转换成功")
                

if __name__ == "__main__":
    inkscapePath = ''
    folder = ''
    convertSVGtoEMF(inkscapePath, folder).startcovert()

    