#-*- encoding:UTF-8 -*-
#可以运行在window任务计划中，
#需要计算的文件太多，该脚本在pycharm直接运行会导致Python.exe内存满，出错
import arcpy,os
from arcpy import env
from arcpy.sa import *
# Tool Name: 遍历要素裁剪栅格
# Created: 2020/2/20
#enveriment setting
env.workspace = r"F:\hourmergepercitation\2016_18"
#设置输出目录地址
outputspace=r"F:\hourmergepercitation\2015_2018ncclip"
#os.listdir方法获取files（所有文件）
files=os.listdir(env.workspace)
#创建一个文件用来计数
with open(r"D:\learn\clipnc4_arcpy\para.txt", 'r') as f:
    i=int(f.read())
    print i
#读取目录下所有nc格式文件
inNetCDFFiles=[]
for file in files:
    if os.path.splitext(file)[1]=='.nc':
        inNetCDFFiles.append(file)
print len(inNetCDFFiles[1000*i:1000*(i+1)])
start=1000*i
if 1000*(i+1)<=len(inNetCDFFiles):
    end=1000*(i+1)
else:
    end=len(inNetCDFFiles)
#定义一个矩形,裁剪区域
#polyPoints = [arcpy.Point(115.7,23.5), arcpy.Point(115.7, 28.4), 
             #arcpy.Point(120.5, 28.4),arcpy.Point(120.5, 23.5)]
with open(r"D:\learn\clipnc4_arcpy\para.txt", 'w') as f:
    f.write(str(i + 1))
    print "write done"
inMaskData = "F:/hourmergepercitation/cliptemp/clippoly84.shp"
for inNetCDFFile in inNetCDFFiles[start:end]:
    rain_layer=os.path.splitext(inNetCDFFile)[0]#获取文件名
    print inNetCDFFile
    #运行前先用arcmap里面工具打开看看文件属性，（通过Python的netcdf4包构建的nc）是"lon"和"lat",
    #国家气象业务中心下载的是"longitude"和"latitude"，这里运行的时候要修改，否者会出错
    arcpy.MakeNetCDFRasterLayer_md(inNetCDFFile, "rain","longitude", "latitude",rain_layer, "", "","BY_VALUE")
    #对栅格图层进行裁剪
    arcpy.CheckOutExtension("spatial")
    outExtractByMask = ExtractByMask(rain_layer, inMaskData)
    #进行重采样成0.01网格
    resamplelayer=outputspace+"/"+rain_layer+".tif" #设置重采样图层输出位置
    arcpy.Resample_management(outExtractByMask, resamplelayer, "0.01", "NEAREST")
    print "resample success"

    #栅格数据保存为tif栅格格式
    #resamplelayer.save("F:/hourmergepercitation/cliptemp/2016/clip2tif"+"/"+rain_layer+".tif")
    #print "Done"


