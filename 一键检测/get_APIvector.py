#coding=gbk
import os

#�ýű���������xml��Ӧ��Ȩ��д�����ݼ���ÿ�������Ӧ���ݼ��е�һ���ļ���ÿ���ļ�ֻ��һ�У�Ϊ��������������97ά����ӦȨ���б��97����ͬȨ��

def getAPIVector(File_Name,Target_path):

    try:
        PermissionList_Path = "./API�б�-�������ݿ�.txt"
        PermissionList = []

        for line in open(PermissionList_Path):
            PermissionList.append(line[:-1])
#        print(PermissionList)
#        print(len(PermissionList))
        PermissionTuple = tuple(PermissionList)
        PermissionExistList=[0]*len(PermissionTuple)

        #����API��Ӧ���ֵ�
        PermissionDictionary=dict(zip(PermissionTuple,PermissionExistList))


        #�洢�õ���API����ÿһ�ж�Ӧһ���ļ�
        ResultList=[]
        ResultList.append(PermissionList)

        i=0
        for line_target in open(File_Name,encoding='utf-8'):
            for key in PermissionDictionary:
                if key in line_target:
                    PermissionDictionary[key]+=1

        TempList=[]
        #    TempList.append(apkName)
        for key in PermissionList:
                TempList.append(int(PermissionDictionary[key]>0))
                PermissionDictionary[key]=0
        #        if PermissionDictionary[key]:
        #            print(apkName)
        #            print("����Ȩ�ޣ�",key)

        with open(Target_path, 'w') as f:
            f.write(str(TempList))
        #    i+=1
    except:
        return False

    return True
