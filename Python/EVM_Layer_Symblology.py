# Import system modules
import arcpy

# Set the current workspace
arcpy.env.workspace = r"C:\Users\JAW\Documents\ArcGIS\Projects\EVM\Sierra\El_Dorado\El_Dorado_2101\Tiger_Lily_2\TigerLily_2.gdb"


##PROJECTS LAYER
# Set layer to apply symbology to
inputLayer = "Projects"

# Set layer that output symbology will be based on
symbologyLayer = r"N:\PROJECTS\PG&E\PGE_ELECTRIC\PGE_EVM\LYR SYMBOLOGY\Vegetation Project.lyr"

# Set the symbology type and fields to be used
field_type = "VALUE_FIELD"
source_field = "STATUS"
target_field = "Status"
symbologyFields = [[field_type, source_field, target_field]]

# Set to update symbology
update_symbology = "DEFAULT"


# Apply the symbology from the symbology layer to the input layer
arcpy.ApplySymbologyFromLayer_management (inputLayer, symbologyLayer, symbologyFields, update_symbology)


##
##PARCELS LAYER
# Set layer to apply symbology to
inputLayer = "Parcels"

# Set layer that output symbology will be based on
symbologyLayer = r"N:\PROJECTS\PG&E\PGE_ELECTRIC\PGE_EVM\LYR SYMBOLOGY\EVM Parcels.lyr"

# Set the symbology type and fields to be used
field_type = "VALUE_FIELD"
source_field = "ACKNOWLEDGE"
target_field = "ACKNOWLEDGE"
symbologyFields = [[field_type, source_field, target_field]]

# Set to update symbology
update_symbology = "DEFAULT"


# Apply the symbology from the symbology layer to the input layer
arcpy.ApplySymbologyFromLayer_management (inputLayer, symbologyLayer, symbologyFields, update_symbology)





##
##PRIMARY CONDUCTOR LAYER
# Set layer to apply symbology to
inputLayer = "Primary_Conductor"

# Set layer that output symbology will be based on
symbologyLayer = r"N:\PROJECTS\PG&E\PGE_ELECTRIC\PGE_EVM\LYR SYMBOLOGY\Conductor Inspection.lyr"

# Set the symbology type and fields to be used
field_type = "VALUE_FIELD"
source_field = "INS_STATUS"
target_field = "INS_STATUS"
symbologyFields = [[field_type, source_field, target_field]]

# Set to update symbology
update_symbology = "DEFAULT"


# Apply the symbology from the symbology layer to the input layer
arcpy.ApplySymbologyFromLayer_management (inputLayer, symbologyLayer, symbologyFields, update_symbology)

