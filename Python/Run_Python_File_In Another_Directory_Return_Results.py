# %%
####STEP 1 Name the file you want to search for and run.
#########Import Project Parent folder variable. Stored in same directory as this file.
import glob, os, subprocess
from Project_Parent_Folder import *

#### Change only this variable ##################################################
file_name_to_run = 'PGE_EA_Sierra_South_Inspection_Tags_Edit_History_Last_Ran.py'
#################################################################################
########### Leave code below alone
####STEP 2 Get the absolute path of the file you want to run
file_path_of_file = glob.glob(Project_Parent_Folder + '\**'+'\\'+file_name_to_run, recursive = True)[0]
####STEP 3 Get the parent folder of the above file and change the cwd to that dir
cwd = os.path.dirname(os.path.abspath(file_path_of_file))
os.chdir(cwd)

# %%
####STEP 4 Run file
output = subprocess.check_output(["python", file_name_to_run], text=True)

# %%
