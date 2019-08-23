# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:\Users\JAW\Documents\ArcGIS\Projects\BidPackage7_OwnershipCheck\BidPackage7_OwnershipCheck.gdb"
#arcpy.env.qualifiedFieldNames = False


# Set JOIN variables
in_layer_or_view = "TM_Parcels_Div05"
in_field = "APN"
join_table = "PCP190613"
join_field = "APN"
join_type = "KEEP_COMMON"


expression = "vegtable.HABITAT = 1"
outFeature = "TM_Parcels_Div05_JOIN_1"



# Join the feature layer to a table
TM_Parcels_Div05_join_table = arcpy.AddJoin_management(in_layer_or_view, in_field, join_table, join_field, join_type)



# Copy the layer to a new permanent feature class
arcpy.CopyFeatures_management(TM_Parcels_Div05_join_table, outFeature)

