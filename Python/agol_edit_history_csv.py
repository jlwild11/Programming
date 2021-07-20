#%%
import os, sys
import datetime
import pandas as pd
import numpy as np
from arcgis import GIS
import keyring
import logging
#%%
#######################################
######Date_Time and Current Dir########
#######################################
#region
#date-time variables
today_now = datetime.datetime.now()
date_time = today_now.strftime("%Y%m%d_%H%M")
backup_day = today_now.strftime("%A")

#%%
# Directory of this python script
current_dir = os.path.dirname(os.path.realpath(__file__))
print(current_dir)


def create_directory_if_doesnt_exist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

#endregion
#%%
################################
######VARIABLES - folder########
################################
#region
process_name = "PGE_EA_Sierra_North_IT_Edit_History_CSV"

folder_name = "Edit_and_Attach_History_csv"

export_dir = os.path.dirname(current_dir) +"\\"+ folder_name
create_directory_if_doesnt_exist(export_dir)
#endregion
#%%
#######################
######Logging########
#######################
#region
#CSV Log variables
log_dts = today_now
log_dts_str = date_time

#Set variables to create a .log log
log_folder_dir = export_dir + "\\" + "Log"
log_file_dot_log = log_folder_dir + "\\" + process_name + "_Log.log"
create_directory_if_doesnt_exist(log_folder_dir)

# Gets or creates a logger
logger = logging.getLogger(__name__)
# set log level
logger.setLevel(logging.INFO)
# define file handler and set formatter
file_handler = logging.FileHandler(log_file_dot_log)
stdout_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : Line No %(lineno)d : %(message)s')
file_handler.setFormatter(formatter)
# add file handler to logger
logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

logger.info('Modules imported, date-time variables set.')
logger.info('Current Directory: '+ current_dir)
logger.info('Process Name: '+ process_name)
logger.info('Folder Name: '+ folder_name)
logger.info('Export Directory: '+ export_dir)
logger.info('Logger created and logging.')

time_end = datetime.datetime.now()-today_now
logger.info('Time Taken: '+ str(time_end))
#endregion
#%%
##################################
######VARIABLES - editable########
##################################
#region
time_start = datetime.datetime.now()
export_type = ".csv"

edit_history_folder_name = "Edit_History"
attach_history_folder_name = "Attachments_History"

edit_history_folder_dir = export_dir +"\\"+ edit_history_folder_name
attach_history_folder_dir = export_dir +"\\"+ attach_history_folder_name
create_directory_if_doesnt_exist(edit_history_folder_dir)
create_directory_if_doesnt_exist(attach_history_folder_dir)

#************************************************************
edit_history_name = "PGE_EA_Sierra_North_IT_Edit_History"
attach_history_name = "PGE_EA_Sierra_North_IT_Attachments_History"
#************************************************************

edit_history_path = edit_history_folder_dir +"\\"+ edit_history_name + export_type
attach_history_path = attach_history_folder_dir +"\\"+ attach_history_name + export_type

#************************************************************
#Be sure column names here match the column names in the 'Variables Not to Edit' section
edit_history_cols_to_add = ['AGOL_GlobalID', 'AGOL_GlobalID_EditDate', 'Deleted', 'Deletion_Recorded_Date']
attach_history_cols_to_add = ['AGOL_PARENTOBJECTID', 'AGOL_ID', 'AGOL_PARENTGLOBALID', 'AGOL_GlobalID', 'Attached_Date', 'Deleted', 'Deleted_Date', 'Export_Name']
            ###Export_Name calculated as AGOL_PARENTGLOBALID +";"+ AGOL_GlobalID +";"+ NAME
#************************************************************

#************************************************************
agol_feature_service_url = "https://services7.arcgis.com/K7kPjayR3FQAPcBi/arcgis/rest/services/service_a00b85ef99554230969025f79a067df2/FeatureServer/1"
agol_feature_service_id = "00fed63e431f4ef1889dc813abc8ed8a"
agol_feature_service_layer_item_num=1
#************************************************************

#************************************************************
###Adjust query to select only veg poitns you need. "(1=1)" selects everything.
#query_add_on = "(vegetation_point_id = 'VP_20210104_084429_39.27279252-120.9774034')"
agol_where_query = "(1=1)" #+ " AND " + query_add_on
#************************************************************

#************************************************************
#list of agol columns to move to front after creating df
move_cols = ['SHAPE']
#************************************************************

###Column names to use to compare and update differences
#************************************************************
#Confirm GlobalID used with your agol feature service.  Possible options are: globalid, GlobalID, GLOBALID, GlobalID_, GLOBALID_1
col_agol_fs_globalid = 'globalid'
#############################
#************************************************************
#endregion

###################################
######VARIABLES Not To Edit########
###################################
#region
col_agol_fs_agol_globalid = 'AGOL_GlobalID'
col_agol_fs_editdate = 'EditDate'
col_agol_fs_agol_globalid_editdate = 'AGOL_GlobalID_EditDate'


col_agol_attach_oid = 'PARENTOBJECTID'
col_agol_attach_id = 'ID'


col_eh_csv_agol_globalid = 'AGOL_GlobalID'
col_eh_csv_agol_globalid_editdate = 'AGOL_GlobalID_EditDate'
col_eh_csv_deleted = 'Deleted'
col_eh_csv_deletion_recorded_date = 'Deletion_Recorded_Date'


col_ah_csv_agol_globalid = 'AGOL_GlobalID'
col_ah_csv_attached_date = 'Attached_Date'
col_ah_csv_deleted = 'Deleted'
col_ah_csv_delete_recorded_date = 'Deletion_Recorded_Date'
col_ah_csv_export_name = 'Export_Name'



agol_attach_oid_download_list = []
agol_attach_id_download_list = []

attach_history_downloads_folder_name = "Attachment_Downloads"
attach_history_downloads_folder_dir = attach_history_folder_dir +"\\"+ attach_history_downloads_folder_name
create_directory_if_doesnt_exist(attach_history_downloads_folder_dir)

time_end = datetime.datetime.now()-time_start
logger.info('Variables created.'+'  Time Taken: '+ str(time_end))
#endregion
#%%
#######################
######FUNCTIONS########
#######################
#region
time_start = datetime.datetime.now()

def move_cols_to_front(df, cols_to_move):
    cols = df.columns.tolist()
    for i in reversed(cols_to_move):
        cols.insert(0, cols.pop(cols.index(i)))
    df = df.reindex(columns=cols)
    return df


def create_empty_csv_if_csv_not_exist(filepath,df):
    if not os.path.exists(filepath):
        df_empty = df[0:0]
        df_empty.to_csv (filepath, index = False, mode='w', header=True)


def add_cols_to_df_if_missing(df,col_list):
    for col in col_list:
        if col not in df:
            df[col] = np.nan


def write_df_back_to_csv(filepath,df):
    df.to_csv (filepath, index = False, mode='w', header=True, date_format='%m/%d/%Y %H:%M:%S')


def date_columns_localize_to_timezone_then_convert_and_remove_timezone(dataframe, localize_timezone = 'UTC', convert_to_timezone = 'US/Pacific'):
    df_timezones_localized = dataframe
    df_date_cols = df_timezones_localized.select_dtypes(include=['datetime64'])
    date_columns_list = list(df_date_cols.columns)
    for x in date_columns_list:
        df_timezones_localized[x] = df_timezones_localized[x].dt.tz_localize(localize_timezone).dt.tz_convert(convert_to_timezone).dt.tz_localize(None)
    dataframe = df_timezones_localized
    return dataframe


def append_df_to_csv(filepath,df):
    if os.path.exists(filepath):
        df.to_csv (filepath, index = False, mode='a', header=False, date_format='%m/%d/%Y %H:%M:%S')
    else:
        df.to_csv (filepath, index = False, mode='w', header=True, date_format='%m/%d/%Y %H:%M:%S')


time_end = datetime.datetime.now()-time_start
logger.info('Functions created.'+'  Time Taken: '+ str(time_end))
#endregion
#%%
#######################
######AGOL Login#######
#######################
#region
time_start = datetime.datetime.now()
system = "AGOL"
username = "mge_gis"
#password = ""
##store password with:
#keyring.set_password(system, username, password)
password = keyring.get_password(system, username)
gis = GIS("https://arcgis.com", username, password)

time_end = datetime.datetime.now()-time_start
logger.info('Logged into AGOL.'+'  Time Taken: '+ str(time_end))
#endregion
#%%
##################################################
######Do Not Edit From Here to End of Script######
##################################################

######################################
######Get AGOL FS and Create DF#######
######################################
#region
time_start = datetime.datetime.now()
item = gis.content.get(agol_feature_service_id)
flayer = item.layers[agol_feature_service_layer_item_num]

time_end = datetime.datetime.now()-time_start
logger.info('AGOL layer got.'+'  Time Taken: '+ str(time_end))
#%%
time_start = datetime.datetime.now()
agol_df = flayer.query(where=agol_where_query).sdf

time_end = datetime.datetime.now()-time_start
logger.info("AGOL layer queried and set to variable 'agol_df'."+'  Time Taken: '+ str(time_end))
#endregion
#%%
###############################################
######Organize and sync columns in eh_df#######
###############################################
#region
time_start = datetime.datetime.now()
agol_df
#%%
agol_df = move_cols_to_front(agol_df,move_cols)
#%%
agol_df
#%%
create_empty_csv_if_csv_not_exist(edit_history_path,agol_df)
eh_df = pd.read_csv(edit_history_path)
#%%
eh_df
#%%
#compare columns in each, add missing columns if needed
missing_agol_col_list = agol_df.columns.difference(eh_df.columns)
#%%
missing_agol_col_list
#%%
#add columns that are in agol_df but are not in eh_df to end of eh_df
for x in missing_agol_col_list:
    eh_df[x] = np.nan
#%%
eh_df
#%%
#add edit_history_cols_to_add to eh if don't exist
add_cols_to_df_if_missing(eh_df,edit_history_cols_to_add)
#%%
eh_df

time_end = datetime.datetime.now()-time_start
logger.info("Edit History columns organized to match agol_df"+'  Time Taken: '+ str(time_end))
#endregion
#%%
###################################################
######Find new columns in eh_df and organize#######
###################################################
#region
time_start = datetime.datetime.now()
#Find new cols in eh that were not made with this script.  
#They will be added to the new col order for the eh and agol dfs
new_eh_col_list = eh_df.columns.difference(agol_df.columns).to_list()
#%%
new_eh_col_list
#%%
#exclude the edit_history_cols_to_add columns.  We can alwys add a column to 
#the edit_history_cols_to_add variable if we need it in a particular order.
new_eh_col_list = list(set(new_eh_col_list).union(set(edit_history_cols_to_add))  - set(new_eh_col_list).intersection(set(edit_history_cols_to_add)))

#%%
new_eh_col_list
#%%
#order columns in eh to same order of agol_df
agol_cols = agol_df.columns.tolist()
#%%
agol_cols
#%%
eh_col_list = edit_history_cols_to_add + new_eh_col_list + agol_cols
#%%
eh_col_list
#%%
eh_df = eh_df.reindex(columns=eh_col_list)
#%%
eh_df
#%%
#write df back to csv to get columns in csv in correct order and new columns added
write_df_back_to_csv(edit_history_path,eh_df)

time_end = datetime.datetime.now()-time_start
logger.info("New columns in Edit History found and re-organized"+'  Time Taken: '+ str(time_end))
#endregion
#%%
#################################################
######Organize and sync columns in agol_df#######
#################################################
#region
time_start = datetime.datetime.now()
#add new eh cols and edit_history_cols_to_add to agol_df to make appending data later easier
all_cols_to_add = edit_history_cols_to_add + new_eh_col_list
add_cols_to_df_if_missing(agol_df,all_cols_to_add)
#%%
agol_df
#%%
agol_df = move_cols_to_front(agol_df,all_cols_to_add)
#%%
agol_df
time_end = datetime.datetime.now()-time_start
logger.info("Columns added to agol_df and organized."+'  Time Taken: '+ str(time_end))
#endregion
#%%
#####################################################
######Change agol_df dates from utc to pacific#######
#####################################################
#region
time_start = datetime.datetime.now()
agol_df = date_columns_localize_to_timezone_then_convert_and_remove_timezone(agol_df, localize_timezone = 'UTC', convert_to_timezone = 'US/Pacific')
#%%
agol_df.head(1)
time_end = datetime.datetime.now()-time_start
logger.info("agol_df date columns converted to UTC."+'  Time Taken: '+ str(time_end))
#endregion
# %%
##############################################
######Calc columns and record new edits#######
##############################################
#region
time_start = datetime.datetime.now()

#calc the col_agol_fs_agol_globalid. Remove brackets{}, make lowercase and strip white space.
agol_df[col_agol_fs_agol_globalid] = agol_df[col_agol_fs_globalid]
agol_df[col_agol_fs_agol_globalid] = agol_df[col_agol_fs_agol_globalid].str.replace("{","",case = False)
agol_df[col_agol_fs_agol_globalid] = agol_df[col_agol_fs_agol_globalid].str.replace("}","",case = False)
agol_df[col_agol_fs_agol_globalid] = agol_df[col_agol_fs_agol_globalid].str.lower()
agol_df[col_agol_fs_agol_globalid] = agol_df[col_agol_fs_agol_globalid].str.strip()
#%%
agol_df.head(1)
# %%
#calc the col_agol_fs_agol_globalid_editdate and strip white space.
agol_df[col_agol_fs_agol_globalid_editdate] = agol_df[col_agol_fs_agol_globalid] +"_"+ agol_df[col_agol_fs_editdate].apply(lambda x: x.strftime('%Y%m%d_%H%M%S'))
agol_df[col_agol_fs_agol_globalid_editdate] = agol_df[col_agol_fs_agol_globalid_editdate].str.strip()
#%%
agol_df.head(1)
time_end = datetime.datetime.now()-time_start
logger.info("agol_df columns calculated."+'  Time Taken: '+ str(time_end))
# %%
time_start = datetime.datetime.now()
#Create col to display if a row has been added to the edit history layer or not.
agol_df['Edit_Recorded'] = agol_df[col_agol_fs_agol_globalid_editdate].isin(eh_df[col_eh_csv_agol_globalid_editdate])
#%%
agol_df.head(1)
# %%
#Create a filter with only new edits
agol_df_new_edits_filter = agol_df["Edit_Recorded"].isin([False])

# %%
agol_df_new_edits = agol_df[agol_df_new_edits_filter]

# %%
agol_df_new_edits

# %%
agol_df_new_edits.drop(['Edit_Recorded'], axis='columns', inplace=True)

# %%
#rows to append to the edit history csv
agol_df_new_edits
# %%
count = len(agol_df_new_edits)
# %%
count
# %%
if count>0:
    append_df_to_csv(edit_history_path,agol_df_new_edits)
    print(str(count) +" rows added. Edit History updated")
else:
    print(str(count) +" rows to add. Edit History updated")

time_end = datetime.datetime.now()-time_start
logger.info("New edits filtered and appended to edit history"+'  Time Taken: '+ str(time_end))
#endregion
# %%
##################################
######Update deleted points#######
##################################
#region
time_start = datetime.datetime.now()

eh_df = pd.read_csv(edit_history_path)
#%%
#the ~ character creates the inverse result. ~ makes the expression read 'not in' rather than 'is in'.
eh_df['Deleted_GlobalID'] = ~eh_df[col_eh_csv_agol_globalid].isin(agol_df[col_agol_fs_agol_globalid])
#%%
eh_df['Deleted_Date_Entered'] = ~eh_df[col_eh_csv_deletion_recorded_date].isnull()
# %%
eh_df
#%%
#create a df of only newly deleted globalids
deleted_df = eh_df[(eh_df['Deleted_GlobalID'] == True) & (eh_df[col_eh_csv_deleted] != 'Deleted') & (eh_df['Deleted_Date_Entered'] == False)]
# %%
#calculate 'Deleted' column for newly deleted globalids
eh_df.loc[(eh_df['Deleted_GlobalID'] == True) & (eh_df[col_eh_csv_deleted] != 'Deleted'), col_eh_csv_deleted] = "Deleted"
# %%
#calculate 'Deletion_Recorded_Date' column for newly deleted globalids
eh_df.loc[(eh_df['Deleted_GlobalID'] == True) & (eh_df['Deleted_Date_Entered'] == False), col_eh_csv_deletion_recorded_date] = today_now
# %%
eh_df
# %%
eh_df.drop(['Deleted_GlobalID','Deleted_Date_Entered'], axis='columns', inplace=True)
# %%
eh_df
#%%
deleted_df
#%%
count = len(deleted_df)
# %%
count
# %%
if count>0:
    write_df_back_to_csv(edit_history_path,eh_df)
    print(str(count) +" deleted records. Deleted records updated")
else:
    print(str(count) +" deleted records. No records updated as 'Deleted'")

time_end = datetime.datetime.now()-time_start
logger.info("Deleted points filtered and Edit History updated."+'  Time Taken: '+ str(time_end))
#endregion
# %%
#########################################
#####Create log file and write to it#####
#########################################
#region
time_start = datetime.datetime.now()

#Set variables to create a csv log
log_folder_dir = export_dir + "\\" + "Log"
log_file = log_folder_dir + "\\" + process_name + "_Log.csv"
create_directory_if_doesnt_exist(log_folder_dir)

#write log variables
log_dtf = datetime.datetime.now()
log_dtf_str = log_dtf.strftime("%Y%m%d_%H%M")
log_ttr = log_dtf - log_dts
log_cols = {'Date_Time_Started_str':[log_dts_str],'Date_Time_Started':[log_dts],'Date_Time_Finished_str':[log_dtf_str],'Date_Time_Finished':[log_dtf],'Time_To_Run':[log_ttr]}
# %%
#create csv log if doesnt exist and write
log_df = pd.DataFrame(log_cols)
# %%
if os.path.exists(log_file):
    log_df.to_csv (log_file, index = False, mode='a', header=False, date_format='%m/%d/%Y %H:%M:%S')
else:
    log_df.to_csv (log_file, index = False, mode='w', header=True, date_format='%m/%d/%Y %H:%M:%S')

logger.info("CSV log updated."+'  Time Taken: '+ str(time_end))

time_end = datetime.datetime.now()-today_now
logger.info("Edit History Script finished."+'  Time Taken: '+ str(time_end))
#endregion
# %%
