# Name: PCTM_Export_Photo_Attachments_script.py
# Purpose: Export photos from an attachments table to a folder

# Import system modules
arcpy.AddMessage("Modules Loading")
import arcpy
from arcpy import da
import os
from datetime import datetime
arcpy.AddMessage("Modules Loaded")

# Set environment settings
arcpy.AddMessage("Environment Settings Loading")
arcpy.env.workspace = r"N:\PROJECTS\PLACER_COUNTY\500_GIS_DATA\Misc\Toolboxes\PCTM_SCRATCH_SPACE.gdb"
workspace = r"N:\PROJECTS\PLACER_COUNTY\500_GIS_DATA\Misc\Toolboxes\PCTM_SCRATCH_SPACE.gdb"
arcpy.env.qualifiedFieldNames = False
arcpy.AddMessage("Environment Settings Loaded")

# Set parameters
arcpy.AddMessage("Parameters Loading")
inFC = arcpy.GetParameterAsText(0)
inFC_ATTACH_Table = arcpy.GetParameterAsText(1)
ParcelLayer = arcpy.GetParameterAsText(2)
exportPhotoLocation = arcpy.GetParameterAsText(3)
arcpy.AddMessage("Parameters Loaded")


# Set Variables
arcpy.AddMessage("Variables Loading")
joinField = "APN"
joinFieldGlobal = "REL_GLOBALID"
joinFieldGlobal2 = "GlobalID_2"
datestring = str(datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S'))
ATTACHExportTable = str("ATTACHExportTable_" + datestring)
arcpy.AddMessage("Variables Loaded")

#AddJoin Parcels to Tree Points by APN
arcpy.AddMessage("AddJoin Parcels to Trees Starting")
joinFC_Tree_Parcels =  arcpy.AddJoin_management(inFC, joinField, ParcelLayer, joinField)
arcpy.AddMessage("AddJoin Parcels to Trees Complete")

#AddJoin Tree Point to ATTACHMENTS Table by GlobalID
arcpy.AddMessage("Add Join to Attach Table Starting")
attachJoin = arcpy.AddJoin_management(inFC_ATTACH_Table, joinFieldGlobal, joinFC_Tree_Parcels, joinFieldGlobal2)
arcpy.AddMessage("Add Join to Attach Table Complete")

# Copy the layer to a new permanent feature class
# Output fields are unqualified, so the field name will 
# not contain the origin table
arcpy.AddMessage("Export Table Being Created")
ExportAttachTable = arcpy.TableToTable_conversion(attachJoin, workspace, ATTACHExportTable)
DupStatsTableName = workspace + "\\" + ATTACHExportTable + "_DUP_Tree_ID_COUNT"
DupStatsTable = DupStatsTableName
arcpy.AddMessage("Export Table Created")


arcpy.AddMessage("Photo Export Starting")
with da.SearchCursor(ExportAttachTable, ['DATA', 'DIVISION', 'APN', 'TREE_ID', 'LAT', 'LONG', 'STREET_NUM', 'STREET_NAME', 'STREET_TYPE','WORK_TYPE', 'ATT_NAME' ]) as cursor:
    for item in cursor:
        attachment = item[0]
        filename = str(item[1]) + "_" + str(item[2]) + "_" + str(item[3]) + "_" + str(item[4]) + "_" + str(item[5]) + "_" + str(item[6]) + " " + str(item[7]) + " " + str(item[8]) + "_" + str(item[9]) + "_" + str(item[10])
        open(exportPhotoLocation + os.sep + filename, 'wb').write(attachment.tobytes())
        del item
        del filename
        del attachment

arcpy.AddMessage("Photo Export Finished")

# Create a Summary table to show duplicate tree photos
arcpy.AddMessage("Duplicate Stats Table Being Created")
arcpy.analysis.Statistics(ExportAttachTable, DupStatsTable , "TREE_ID COUNT", "TREE_ID")
arcpy.AddMessage("Duplicate Stats Table Created")


arcpy.AddMessage("Script Finished")
arcpy.AddMessage("Any data created to complete this script is stored in: ")
arcpy.AddMessage("N:\PROJECTS\PLACER_COUNTY\500_GIS_DATA\Misc\Toolboxes\PCTM_SCRATCH_SPACE.gdb")