#!/usr/bin/env python
#coding: utf-8
import os
# 获得与该计算机连接的所有外接设备名称
# 源目录
deviceFilePath = '/sys/class/input/'

def showDevice():
    os.chdir(deviceFilePath)
    for i in os.listdir(os.getcwd()):
        namePath = deviceFilePath + i + '/device/name'
        if os.path.isfile(namePath):
            print "Name: %s Device: %s" % (i, file(namePath).read())


if __name__ =="__main__":
    showDevice()
