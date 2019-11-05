import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/GreenvalleyDB.gdb/Public Buildings"

arcpy.FeatureClassToFeatureClass_conversion("buildings_point", 
                                            "C:/output/output.gdb", 
                                            "buildings_point")
