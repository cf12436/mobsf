#coding=gbk
import static_analyzer
import Main
import API_Test_Single
import API_Test_Single1
import os
import datetime
APIvector_Path = "E:/mobsf/Mobsf/StaticAnalyzer/views/android/API_vector/"
'''       
     app_file = app_dic['md5'] + '.apk'  # NEW FILENAME
     app_path = app_dic['app_dir']+ app_file  # APP PATH            
     Filepath = app_path
     print("Firepath:", Filepath)
     ErrorList = []                  
     if not Main.main(Filepath):
        ErrorList.append(Filepath)
     print(ErrorList)
     print("Main.main(Filepath)", Main.main(Filepath))
     detection_result = API_Test_Single.detection(Main.APIvector_Path)
     print("detection_result", detection_result)
     for index,key in enumerate(os.listdir(Main.APIvector_Path)):
         if Main.output_result(detection_result[index])==1:
             print("######################################################################")
             print(key[:-4],"程序评分：",detection_result[index],"  参考结果为：",Main.output_result(detection_result[index]))
             print("######################################################################")
         else:
             print("######################################################################")
             print("未发现恶意程序...","参考结果为：",Main.output_result(detection_result[index]))
             print("######################################################################")
'''
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
    print("delete file ")
# def function(str):
#     t1= datetime.datetime.now()
#   #  print(static_analyzer.app_dic['md5'])
#   #  app_file = static_analyzer.app_dic['md5'] + '.apk'  # NEW FILENAME
#   #  app_path = static_analyzer.app_dic['app_dir'] + app_file  # APP PATH
#     Filepath = str
#     print("Firepath:", Filepath)
#     ErrorList = []
#     if not Main.main(Filepath):
#         ErrorList.append(Filepath)
#         print(ErrorList)
#     detection_result = API_Test_Single.detection(Main.APIvector_Path)
#     print("detection_result", detection_result)
#     is_good=0
#     for index, key in enumerate(os.listdir(Main.APIvector_Path)):
#         if Main.output_result(detection_result[index]) == 1:
#             print("发现异常",index)
#             print(key[:-4],"程序评分：",detection_result[index],"  参考结果为：",Main.output_result(detection_result[index]))
#             is_good+=1
#     if(is_good):
#         judge="恶意程序"
#     else:
#         judge="良性程序"
#     t2= datetime.datetime.now()
#     del_file(Main.APIvector_Path)
#     print(judge)
#     print("costtime:",(t2-t1).seconds)
#     return judge
def function(str):
    t1= datetime.datetime.now()
  #  print(static_analyzer.app_dic['md5'])
  #  app_file = static_analyzer.app_dic['md5'] + '.apk'  # NEW FILENAME
  #  app_path = static_analyzer.app_dic['app_dir'] + app_file  # APP PATH
    Filepath = str
    print("Firepath:", Filepath)
    ErrorList = []
    if not Main.main(Filepath):
        ErrorList.append(Filepath)
        print(ErrorList)
    detection_result = API_Test_Single.detection(Main.APIvector_Path)
    print("detection_result", detection_result)
    is_good=0
    for index, key in enumerate(os.listdir(Main.APIvector_Path)):
        if Main.output_result(detection_result[index]) == 1:
            print("发现异常",index)
            print(key[:-4],"程序评分：",detection_result[index],"  参考结果为：",Main.output_result(detection_result[index]))
            is_good+=1
    if(is_good):
        judge="恶意程序"
    else:
        judge = "良性程序"
    t2= datetime.datetime.now()
    del_file(Main.APIvector_Path)
    print("costtime:",(t2-t1).seconds)
    return judge

def function1(str):
    t1= datetime.datetime.now()
  #  print(static_analyzer.app_dic['md5'])
  #  app_file = static_analyzer.app_dic['md5'] + '.apk'  # NEW FILENAME
  #  app_path = static_analyzer.app_dic['app_dir'] + app_file  # APP PATH
    Filepath = str
    print("Firepath:", Filepath)
    ErrorList = []
    if not Main.main(Filepath):
        ErrorList.append(Filepath)
        print(ErrorList)
    print("####这里1#######")
    detection_result1 = API_Test_Single1.detection(APIvector_Path)
    print("####这里2#######")
    print("detection_result", detection_result1)
    is_good1 = 0
    for index, key in enumerate(os.listdir(Main.APIvector_Path)):
        if Main.output_result(detection_result1[index]) == 1:
            print("发现异常",index)
            print(key[:-4],"程序评分：",detection_result1[index],"  参考结果为：",Main.output_result(detection_result1[index]))
            is_good1+=1
    if(is_good1):
        judge1="恶意程序"
    else:
        judge1 = "良性程序"
    t2= datetime.datetime.now()
    del_file(Main.APIvector_Path)
    print("costtime:",(t2-t1).seconds)
    return judge1