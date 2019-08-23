# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:\Users\JAW\Documents\ArcGIS\Projects\TM_Parcels_Master\TM_Parcels_Master.gdb"


# Set APPEND variables
inputs = "https://services7.arcgis.com/K7kPjayR3FQAPcBi/arcgis/rest/services/NEW_ROE_Parcel/FeatureServer/0"
target = "TM_Parcels_Master"
schema_type = "NO_TEST"




# Run APPEND
arcpy.Append_management(inputs, target, schema_type)
