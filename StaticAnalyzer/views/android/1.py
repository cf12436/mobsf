import API_Test_Single1
import API_Test_Single
import os
import Main
APIvector_Path = "E:/mobsf/Mobsf/StaticAnalyzer/views/android/API_vector/"
def output_result(input):
    if input[0]>=input[1]:
        return 0
    else:
        return 1
def function1(str):
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
    return judge1

app_path="F:/appk/天气预报.apk"
target1 = function1(app_path)