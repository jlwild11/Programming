import arcpy
import os

workspace = r"N:\PROJECTS\PLACER_COUNTY\500_GIS_DATA\GDB\Master_Buckets"

walk = arcpy.da.Walk(workspace, datatype="FeatureClass")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        desc = arcpy.Describe(os.path.join(dirpath, filename))
        print (desc.path + "___" + desc.spatialReference.name)

print ("Script completed")


import arcpy
import os

workspace = r"N:\PROJECTS\USFS\IDIQ_2019\South_Fork_SMMU\South_Fork.gdb"

walk = arcpy.da.Walk(workspace, datatype="FeatureClass")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        desc = arcpy.Describe(os.path.join(dirpath, filename))
        print (desc.name + "___" + desc.spatialReference.name)

print ("Script completed")