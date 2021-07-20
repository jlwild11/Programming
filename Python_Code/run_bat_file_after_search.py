def run_bat_file_after_search(file_name, project_parent_folder_path):
    import  subprocess
    file_path = file_path_of_filename_recursive_search(file_name,project_parent_folder_path)
    change_working_directory(file_path)
    subprocess.run(file_name)
    