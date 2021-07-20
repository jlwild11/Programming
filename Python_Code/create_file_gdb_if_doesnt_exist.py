def create_file_gdb_if_doesnt_exist(folder_path, gdb):
    import os, arcpy
    if not os.path.exists(folder_path + "\\" + gdb):
        arcpy.CreateFileGDB_management(folder_path, gdb)
        