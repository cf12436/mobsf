#coding=gbk
import os
import zipfile
import sys
import shutil
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import Decode_dex
import Clearup_dex
import get_APIvector2
import datetime
import API_Test_Single1

APIvector_Path = "E:/mobsf/Mobsf/StaticAnalyzer/views/android/API_vector/"

def main(file_path):
    #创建工作目录，如果已经存在同名目录，会删除掉同名目录，注意这里
    print("开始处理文件",os.path.basename(file_path))
    target_path = file_path[:-4]
    if os.path.exists(target_path):
 #       if tk.messagebox.askyesno("警告","发现存在同名文件夹，即将删除，是否继续"):
        if 1:
            try:
                shutil.rmtree(target_path)
                print("     已删除同名文件夹")
                time.sleep(1)
            except:
                print("     删除失败，已跳过该文件")
                return False
        else:
            print("     跳过该文件")
            return False
    os.mkdir(target_path)

    #读取apk文件并解压缩其中的关键文档
    try:
        z = zipfile.ZipFile(file_path, 'r')
    except:
        return False
    a_name=z.namelist()
    for name in a_name:
        if name == "classes.dex":
            try:
                z.extract(name,target_path)
                print("     成功解压缩class.dex，开始解码")
            except:
                return False
    z.close()

    #调用jar解码文档
    DexPath = os.path.join(target_path,"classes.dex")
    if Decode_dex.Decode(DexPath) == False:
        print("     解码时发生错误，已跳过该文件")
        return False
    else:
        print("     成功解码dex，下面进行整理")

    #整理解码出来的smali
    SmaliPath = DexPath[:-4]

    if not Clearup_dex.clear_up(SmaliPath):
        print("     整理时发生错误，已跳过该文件")
        return False
    else:
        print("     API整理完毕，下面提取向量")

    #从整理好的文档之中获得特征向量
    DextxtPath = SmaliPath + ".txt"
    Target_Path = APIvector_Path + os.path.basename(file_path)[:-4]+".txt"
    if not get_APIvector2.getAPIVector(DextxtPath, Target_Path):
        print("     提取向量时发生错误，跳过该文件")
        return False
    else:
        print("     向量提取完毕，下面删除临时文件")

    #删除临时文件
    try:
        shutil.rmtree(target_path)
        print("     已删除临时文件夹")
        time.sleep(1)
    except:
        print("     删除失败，已跳过该文件")
        return False

    return True

def output_result(input):
    if input[0]>=input[1]:
        return 0
    else:
        return 1


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
    print("delete file ")
if __name__ == '__main__':
    t1 = datetime.datetime.now()
    Filepath = "F:/appk/绿色阅读.apk"
    print(Filepath)
    ErrorList = []
    if not main(Filepath):
        ErrorList.append(Filepath)
    print(ErrorList)
    detection_result = API_Test_Single1.detection(APIvector_Path)
    print(detection_result)
    is_good = 0
    for index, key in enumerate(os.listdir(APIvector_Path)):
        if output_result(detection_result[index]) == 1:
            print("发现异常", index)
            print(key[:-4], "程序评分：", detection_result[index], "  参考结果为：", output_result(detection_result[index]))
            is_good += 1
    if (is_good):
        judge = "恶意程序"
    else:
        judge = "良性程序"
    print(judge)
    t2 = datetime.datetime.now()
    del_file(APIvector_Path)
    print("costtime:", (t2 - t1).seconds)