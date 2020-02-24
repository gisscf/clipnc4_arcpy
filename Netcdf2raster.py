import arcpy
from arcpy import env
from arcpy.sa import *
def NetCDF2Tiff(inNetCDFFile,toTIFFFile):
 
    variable = "rain"
    XDimension = "longitude"
    YDimension = "latitude"
    outRasterLayer = "rain_Layer"
    bandDimmension = ""
    dimensionValues = ""
    valueSelectionMethod = "BY_VALUE"
 
    print "start"
    arcpy.MakeNetCDFRasterLayer_md(inNetCDFFile, variable, XDimension, YDimension,
                                   outRasterLayer, bandDimmension, dimensionValues,
                                   valueSelectionMethod)
    print "done"
    arcpy.CopyRaster_management(outRasterLayer, toTIFFFile)
 
    print "finish"
 
##
# Set environment settings
env.workspace="E:/cliptemp"
# Set local variables
inNetCDFFile = "SURF_CLI_CHN_MERGE_PRE_HOUR_GRID_0.05-2017010100.nc"
toTIFFFile =  "test.tif"
 
NetCDF2Tiff(inNetCDFFile,toTIFFFile)
