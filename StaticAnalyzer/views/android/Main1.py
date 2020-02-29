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
    #��������Ŀ¼������Ѿ�����ͬ��Ŀ¼����ɾ����ͬ��Ŀ¼��ע������
    print("��ʼ�����ļ�",os.path.basename(file_path))
    target_path = file_path[:-4]
    if os.path.exists(target_path):
 #       if tk.messagebox.askyesno("����","���ִ���ͬ���ļ��У�����ɾ�����Ƿ����"):
        if 1:
            try:
                shutil.rmtree(target_path)
                print("     ��ɾ��ͬ���ļ���")
                time.sleep(1)
            except:
                print("     ɾ��ʧ�ܣ����������ļ�")
                return False
        else:
            print("     �������ļ�")
            return False
    os.mkdir(target_path)

    #��ȡapk�ļ�����ѹ�����еĹؼ��ĵ�
    try:
        z = zipfile.ZipFile(file_path, 'r')
    except:
        return False
    a_name=z.namelist()
    for name in a_name:
        if name == "classes.dex":
            try:
                z.extract(name,target_path)
                print("     �ɹ���ѹ��class.dex����ʼ����")
            except:
                return False
    z.close()

    #����jar�����ĵ�
    DexPath = os.path.join(target_path,"classes.dex")
    if Decode_dex.Decode(DexPath) == False:
        print("     ����ʱ�����������������ļ�")
        return False
    else:
        print("     �ɹ�����dex�������������")

    #������������smali
    SmaliPath = DexPath[:-4]

    if not Clearup_dex.clear_up(SmaliPath):
        print("     ����ʱ�����������������ļ�")
        return False
    else:
        print("     API������ϣ�������ȡ����")

    #������õ��ĵ�֮�л����������
    DextxtPath = SmaliPath + ".txt"
    Target_Path = APIvector_Path + os.path.basename(file_path)[:-4]+".txt"
    if not get_APIvector2.getAPIVector(DextxtPath, Target_Path):
        print("     ��ȡ����ʱ���������������ļ�")
        return False
    else:
        print("     ������ȡ��ϣ�����ɾ����ʱ�ļ�")

    #ɾ����ʱ�ļ�
    try:
        shutil.rmtree(target_path)
        print("     ��ɾ����ʱ�ļ���")
        time.sleep(1)
    except:
        print("     ɾ��ʧ�ܣ����������ļ�")
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
    Filepath = "F:/appk/��ɫ�Ķ�.apk"
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
            print("�����쳣", index)
            print(key[:-4], "�������֣�", detection_result[index], "  �ο����Ϊ��", output_result(detection_result[index]))
            is_good += 1
    if (is_good):
        judge = "�������"
    else:
        judge = "���Գ���"
    print(judge)
    t2 = datetime.datetime.now()
    del_file(APIvector_Path)
    print("costtime:", (t2 - t1).seconds)