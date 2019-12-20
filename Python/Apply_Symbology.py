#
#
import arcpy
from datetime import datetime


ExportVegName = ""

ExportParcelName ""

ExportPriCondInspName ""


######SYMBOLOGY
Vegetation_Point_lyr = "C:\\Users\\jaw\OneDrive - Mountain G. Enterprises, Inc\\PGE\\EVM\Symbology\\Vegetation Point.lyr"
EVM_Parcels_lyr = "C:\\Users\\jaw\OneDrive - Mountain G. Enterprises, Inc\\PGE\\EVM\Symbology\\EVM_Parcels.lyr"
Primary_Conductor_Inspection_lyr = "C:\\Users\\jaw\OneDrive - Mountain G. Enterprises, Inc\\PGE\\EVM\Symbology\\Primary Conductor Inspection.lyr"




###### Process: Apply Symbology From Layer to ExportVegName
arcpy.ApplySymbologyFromLayer_management(ExportVegName, Vegetation_Point_lyr)

##### Process: Apply Symbology From Layer to ExportParcelName
arcpy.ApplySymbologyFromLayer_management(ExportParcelName, EVM_Parcels_lyr)

##### Process: Apply Symbology From Layer to ExportPriCondInspName
arcpy.ApplySymbologyFromLayer_management(ExportPriCondInspName, Primary_Conductor_Inspection_lyr)
