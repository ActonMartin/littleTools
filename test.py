import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import os
from PyQt5.QtWidgets import *

global b_img, r_cut_img, w_cut_img, b_img_with_boxes, r_img_with_boxes, g_img_with_boxes, b_cut_img, g_cut_img
global point1, point2, point3, point4
global cnt
global boxes
global args
global key
global select_RGB
global is_draw_boundbox
global rect_info

##[320,320], [240, 120], [120,240]
###########################################################111111##############################################
args = {"iou_width": 320,
        "iou_height": 320,
        "iou_depth": 1,
        "output_prefix_merged": 'G:/ZTEST/201904012-20190418-GKJ2/FRONT/IMAGE_PATCH/',  # 路径千万不能有中文##
        "output_prefix_white": 'G:/ZTEST/201904012-20190418-GKJ2/FRONT/IMAGE_PATCH/',  ##
        "output_prefix_RED": 'G:/ZTEST/201904012-20190418-GKJ2/FRONT/IMAGE_PATCH/',  ##
        "output_prefix_GREEN": 'G:/ZTEST/201904012-20190418-GKJ2/FRONT/IMAGE_PATCH/',  ##
        "output_prefix_BLUE": 'G:/ZTEST/201904012-20190418-GKJ2/FRONT/IMAGE_PATCH/',  ##
        }
########################22222222#################
W_DIR = 'G:/ZTEST/201904012-20190418-GKJ2/FRONT/WHITE/'  ##
R_DIR = 'G:/ZTEST/201904012-20190418-GKJ2/FRONT/RED/'  ##
G_DIR = 'G:/ZTEST/201904012-20190418-GKJ2/FRONT/GREEN/'  ##
B_DIR = 'G:/ZTEST/201904012-20190418-GKJ2/FRONT/BLUE/'  ##



# DEFAIT_DIALOG="E:/anaconda/front_renamed/segmented/classified/"  ##默认对话框打开的位置, 【不用管】


class MainForm(QWidget):
    def __init__(self, image_list, pathes, name='MainForm'):
        super(MainForm, self).__init__()
        self.setWindowTitle(name)
        #self.cwd = DEFAIT_DIALOG  # os.getcwd() # 获取当前程序文件位置
        self.resize(300, 200)  # 设置窗体大小
        self.image_list = image_list
        self.pathes = pathes
        # self.rect_info=rect_info
        # btn 1
        self.btn_chooseDir = QPushButton(self)
        self.btn_chooseDir.setObjectName("btn_chooseDir")
        self.btn_chooseDir.setText("选择文件夹")

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.btn_chooseDir)
        # layout.addWidget(self.btn_saveFile)
        self.setLayout(layout)

        # 设置信号
        self.btn_chooseDir.clicked.connect(self.slot_btn_chooseDir)

    def slot_btn_chooseDir(self):
        dir_choose = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      self.cwd)  # 起始路径
        if dir_choose == "":
            print("\n取消选择")
            return

        # print("\n你选择的文件夹为:")
        # print(dir_choose)
        path_m = dir_choose + "/" + args["file_pre"] + "_" + str(cnt) + "_M" + '.jpg'
        path_r = dir_choose + "/" + args["file_pre"] + "_" + str(cnt) + "_R" + '.jpg'
        path_g = dir_choose + "/" + args["file_pre"] + "_" + str(cnt) + "_G" + '.jpg'
        path_b = dir_choose + "/" + args["file_pre"] + "_" + str(cnt) + "_B" + '.jpg'
        path_w = dir_choose + "/" + args["file_pre"] + "_" + str(cnt) + "_W" + '.jpg'

        cv2.imwrite(path_m, self.image_list["img_merged"])
        cv2.imwrite(path_w, self.image_list["w_cut_img"])
        cv2.imwrite(path_r, self.image_list["r_cut_img"])
        cv2.imwrite(path_g, self.image_list["g_cut_img"])
        cv2.imwrite(path_b, self.image_list["b_cut_img"])

        # txt_filename=dir_choose+'/'+args["file_pre"]+"_"+str(cnt)+".txt"
        # f = open(txt_filename)
        # for rt in self.rect_info:
        #       f.write(str(rt[0])+","+str(rt[1])+","+str(rt[2])+","+str(rt[3])+" ")


def on_mouse(event, x, y, flags, param):
    global b_img, b_cut_img, g_cut_img, r_cut_img, w_cut_img, r_img_with_boxes, g_img_with_boxes, b_img_with_boxes
    global point1, point2, point3, point4, cnt, boxes, box_rect
    global args
    global key
    global select_RGB
    global is_draw_boundbox

    if select_RGB == 0:
        img2 = r_img_with_boxes.copy()
    elif select_RGB == 1:
        img2 = g_img_with_boxes.copy()
    else:
        img2 = b_img_with_boxes.copy()

    global box_rect
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        args["point_x"] = x
        args["point_y"] = y
        # if is_draw_boundbox==False:
        point1 = (x, y)
        cv2.circle(img2, point1, 2, (0, 0, 255), 3)
        cv2.imshow('image', img2)

        # rect_info=[]
        # else:
        # point3=(x,y)
        # cv2.circle(img2, point3, 2, (0,255,0), 3)
        # cv2.imshow('image', img2)

    # elif event == cv2.EVENT_FLAG_CTRLKEY: #滚轮滚动

    #     print(".---------------------------------...")

    elif event == cv2.EVENT_MOUSEWHEEL:  # 滚轮滚动

        select_RGB = select_RGB + 1
        if select_RGB == 3:
            select_RGB = 0

        if select_RGB == 0:
            img2 = r_img_with_boxes.copy()

        elif select_RGB == 1:
            img2 = g_img_with_boxes.copy()

        else:
            img2 = b_img_with_boxes.copy()

        cv2.imshow('image', img2)




    elif event == cv2.EVENT_MBUTTONDOWN:

        cnt += 1
        # img_with_boxes=img2.copy()
        point2 = (args["point_x"] + args["iou_width"], args["point_y"] + args["iou_height"])
        cv2.rectangle(r_img_with_boxes, point1, point2, (0, 0, 255), 3)
        cv2.rectangle(g_img_with_boxes, point1, point2, (0, 0, 255), 3)
        cv2.rectangle(b_img_with_boxes, point1, point2, (0, 0, 255), 3)

        out_path_merged = args["output_prefix_merged"] + args["file_pre"] + "_" + str(cnt) + "_M.jpg"
        out_path_white = args["output_prefix_white"] + args["file_pre"] + "_" + str(cnt) + "_W.jpg"

        out_path_red = args["output_prefix_RED"] + args["file_pre"] + "_" + str(cnt) + "_R.jpg"
        out_path_blue = args["output_prefix_BLUE"] + args["file_pre"] + "_" + str(cnt) + "_B.jpg"
        out_path_green = args["output_prefix_GREEN"] + args["file_pre"] + "_" + str(cnt) + "_G.jpg"

        img_merged = cv2.merge([r_cut_img, g_cut_img, b_cut_img])

        pathes = {"out_path_merged": out_path_merged,
                  "out_path_white": out_path_white,
                  "out_path_red": out_path_red,
                  "out_path_green": out_path_green,
                  "out_path_blue": out_path_blue
                  }

        img_list = {"img_merged": img_merged,
                    "w_cut_img": w_cut_img,
                    "r_cut_img": r_cut_img,
                    "g_cut_img": g_cut_img,
                    "b_cut_img": b_cut_img
                    }
        cv2.imwrite(out_path_merged, img_merged)
        cv2.imwrite(out_path_white, w_cut_img)
        cv2.imwrite(out_path_red, r_cut_img)
        cv2.imwrite(out_path_green, g_cut_img)
        cv2.imwrite(out_path_blue, b_cut_img)

        print(cnt)

        min_x = min(point1[0], point2[0])
        min_y = min(point1[1], point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] - point2[1])

        '''
        #rect_info.append([min_y, min_x, height, width])      
        app = QApplication(sys.argv)
        mainForm = MainForm(img_list, pathes, '选择保存的文件夹')
        mainForm.show()
        try:
             sys.exit(app.exec_())
        except:
             print('window closed')
        '''

    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放
        # if is_draw_boundbox==False:
        point2 = (args["point_x"] + args["iou_width"], args["point_y"] + args["iou_height"])
        cv2.rectangle(img2, point1, point2, (0, 0, 255), 3)
        cv2.imshow('image', img2)

        min_x = min(point1[0], point2[0])
        min_y = min(point1[1], point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] - point2[1])

        b_img_path = B_DIR + args["file_pre"] + '.bmp'
        g_img_path = G_DIR + args["file_pre"] + '.bmp'
        r_img_path = R_DIR + args["file_pre"] + '.bmp'
        w_img_path = W_DIR + args["file_pre"] + '.bmp'

        b_img_to_cut = read_img(args, b_img_path)  # [850:1650, 200:3000]
        g_img_to_cut = read_img(args, g_img_path)  # [850:1650, 200:3000]
        r_img_to_cut = read_img(args, r_img_path)  # [850:1650, 200:3000]
        w_img_to_cut = read_img(args, w_img_path)  # [850:1650, 200:3000]

        b_cut_img = b_img_to_cut[min_y:min_y + height, min_x:min_x + width]
        g_cut_img = g_img_to_cut[min_y:min_y + height, min_x:min_x + width]
        r_cut_img = r_img_to_cut[min_y:min_y + height, min_x:min_x + width]
        w_cut_img = w_img_to_cut[min_y:min_y + height, min_x:min_x + width]
        # else:
        # point4=(args["point_x"]+args["iou_width"], args["point_y"]+args["iou_height"])
        # cv2.rectangle(img2, point3, point4, (0,255,0), 3)
        # cv2.imshow('image', img2)


def read_img(args, path):
    if args["iou_depth"] == 3:
        img = cv2.imread(path, cv2.IMREAD_COLOR)
    elif args["iou_depth"] == 1:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        raise ValueError("args[iou_depth]=%d is an invalid value!" % args["iou_depth"])
    return img


def main():
    global b_img, cnt, cut_img, b_img_with_boxes, g_img_with_boxes, r_img_with_boxes
    global boxes, box_rect
    global args
    global key
    global select_RGB
    global is_draw_boundbox

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    # cv2.namedWindow("image", cv2.WINDOW_KEEPRATIO)

    '''
    cv2.namedWindow("enlarged_image_R", cv2.WINDOW_NORMAL)
    cv2.namedWindow("enlarged_image_G", cv2.WINDOW_NORMAL)
    cv2.namedWindow("enlarged_image_B", cv2.WINDOW_NORMAL)
    '''


    # cv2.namedWindow('image',0)
    pathes = os.listdir(B_DIR)
    pathes_int=[]
    for p in pathes:
           pathes_int.append(int(p.split('.')[0]))
    pathes_int=sorted(pathes_int)

    for pi in range(len(pathes_int)):
        p=str(pi)+".bmp"
        cnt = 0
        if not p.endswith(".bmp"):
            continue
        args["file_pre"] = str(p).split(".")[0]
        r_img_path = R_DIR + p
        g_img_path = G_DIR + p
        b_img_path = B_DIR + p
        w_img_path = W_DIR + p

        print(b_img_path)
        r_img = read_img(args, r_img_path)  # [800:1700, 500:2700]
        g_img = read_img(args, g_img_path)  # [800:1700, 500:2700]
        b_img = read_img(args, b_img_path)  # [800:1700, 500:2700]
        w_img = read_img(args, w_img_path)  # [800:1700, 500:2700]

        select_RGB = 0
        r_img_with_boxes = r_img.copy()
        g_img_with_boxes = g_img.copy()
        b_img_with_boxes = b_img.copy()
        cv2.setMouseCallback('image', on_mouse)
        cv2.imshow('image', b_img_with_boxes)

        '''
        img_eng_R = r_img[850:1650, 200:3000]
        cv2.imshow('enlarged_image_R', img_eng_R)
        img_eng_G = g_img[850:1650, 200:3000]
        cv2.imshow('enlarged_image_G', img_eng_G)
        img_eng_B = b_img[850:1650, 200:3000]
        cv2.imshow('enlarged_image_B', img_eng_B)
        '''


        key = cv2.waitKey(0)
        if key == 32:  # 格键
            continue
        else:
            break


if __name__ == '__main__':
    main()



