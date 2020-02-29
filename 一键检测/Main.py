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
import time
import API_Test_Single
import matplotlib
APIvector_Path = "./API_vector/"
file_path="./apk"
def main(file_path):
    matplotlib.use('Agg')
    #��������Ŀ¼������Ѿ�����ͬ��Ŀ¼����ɾ����ͬ��Ŀ¼��ע������
    print("start:",os.path.basename(file_path))
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
    print("######################################################################")
    print(file_path)
    print(Target_Path)
    print("######################################################################")
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
        return "��������"
    else:
        return "�������"

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    Filepath = filedialog.askopenfilenames(filetypes={('APK', '*.*')},initialdir="./",title="ѡ��һЩapk�ļ��Խ��к����Ĳ���")
    print("######################################################################")
    print("Firepath:", Filepath)
    ErrorList = []
    is_good=0
    for Filename in Filepath:
        if not main(Filename):
            ErrorList.append(Filename)
    print(ErrorList)
    detection_result = API_Test_Single.detection(APIvector_Path)
    for index,key in enumerate(os.listdir(APIvector_Path)):
        if output_result(detection_result[index])=="�������":
            is_good+=1
            print("######################################################################")
            print(key[:-4],"�������֣�",detection_result[index],"  �ο����Ϊ��",output_result(detection_result[index]))
            print("######################################################################")
    if(is_good):
        print("�������")
    else:
        print("���Գ���")
        
  