#coding=utf-8
import os

#���ű���dex�ĵ���������Ϊsmali�ļ���


def Decode(FilePath):
    BaksmaliPath = "./baksmali-2.3.jar"
    try:
        oldPath = FilePath
        newPath = FilePath[:-4]
        cmd = "java -jar " +BaksmaliPath + " d " + oldPath + " -o " + newPath
        os.system(cmd)
    except:
        return False
    return True