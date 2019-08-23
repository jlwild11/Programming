import arcpy
import os

workspace = arcpy.GetParameterAsText(0)

walk = arcpy.da.Walk(workspace, datatype="FeatureClass")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        desc = arcpy.Describe(os.path.join(dirpath, filename))
        print (desc.name + "___" + desc.spatialReference.name)

print ("Script completed")