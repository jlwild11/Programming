#
#
#
ListLayer = "BANGOR_1101_V7_20191219_083850_PrimaryConductorInspection"
ListLayerField = "UNIQUE_SEGMENT_ID"

SelectLayer = "BANGOR_1101_V7_20191219_083850_VegPoints"
SelectLayerField = "UNIQUE_SEGMENT_ID"


###### Create a list of Selected records from a field to be used in a SQL query

List = [row[0] for row in arcpy.da.SearchCursor(ListLayer, ListLayerField)]

SQL_List = "({}{}{})".format("'","','".join([str(n) for n in List]),"'")
#print(SQL_List)

###SQL Expression
ExpressionSelect = "({} IN {})".format(SelectLayerField,SQL_List)
#print(ExpressionSelect)

###### Process: Select Veg Layer By Selected UniqueSegementIDList
arcpy.SelectLayerByAttribute_management(SelectLayer, "NEW_SELECTION", ExpressionSelect)
