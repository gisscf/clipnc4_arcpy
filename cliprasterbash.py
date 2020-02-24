#-*- encoding:UTF-8 -*-
import arcpy,os
import string
from arcpy import env
from arcpy.sa import *
# Tool Name: 遍历要素裁剪栅格
# Created: 2020/2/18
arcpy.CheckOutExtension("spatial")

#enveriment setting
env.workspace = r"L:\hourmergepercitation\2016\201603"

#os.listdir方法获取files（所有文件）
files=os.listdir(env.workspace)
inNetCDFFiles=[]
for file in files:
    if os.path.splitext(file)[1]=='.nc':
        inNetCDFFiles.append(file)
        
inMaskData = "E:/cliptemp/clippoly.shp"
for inNetCDFFile in inNetCDFFiles:
    rain_layer=os.path.splitext(inNetCDFFile)[0][-10:] #获取文件名
    arcpy.MakeNetCDFRasterLayer_md(inNetCDFFile, "rain","longitude", "latitude",
                                   rain_layer, "", "","BY_VALUE")
    outExtractByMask = ExtractByMask(rain_layer, inMaskData)
    outExtractByMask.save("L:/hourmergepercitation/2016/2016clip2tif"+"/"+os.path.splitext(inNetCDFFile)[0][-10:]+".tif")
    print "Done"
    
