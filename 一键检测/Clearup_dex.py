#coding=utf-8
import os

#���ű���FilePath�µ�smali�ļ��е�API������������TargetPath�ж�ӦAPK���ı��ĵ��У����ͺ�����ҵ�ʱ��


def clear_up(FilePath):
    TargetString = ";->"
    try:
        newPath = FilePath
        newName = FilePath + ".txt"
        f = open(newName,"w",encoding='utf-8')
        for root, dirs, files in os.walk(newPath, topdown=False):
            for name in files:
                for line in open(os.path.join(root, name),'r', encoding='UTF-8'):
                    if TargetString in line:
                        f.write(line)
        f.close()
    except:
        return False
    return True