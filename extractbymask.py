# Name: ExtractByMask_Ex_02.py
# Description:
#1.convection from NetCDF to rasterlayer
#2.Extracts the cells of a raster that correspond with the areas
#    defined by a mask.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
# set convect function
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

# Set environment settings
env.workspace = "E:/cliptemp"

# Set local variables
inNetCDFFile = "SURF_CLI_CHN_MERGE_PRE_HOUR_GRID_0.05-2017010100.nc"
toTIFFFile =  "2017010100.tif"
NetCDF2Tiff(inNetCDFFile,toTIFFFile)
inMaskData = "clippoly.shp"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute ExtractByMask
outExtractByMask = ExtractByMask(toTIFFFile, inMaskData)
print "ok"
# Save the output 
outExtractByMask.save(env.workspace+"/"+"optrain.tif")

