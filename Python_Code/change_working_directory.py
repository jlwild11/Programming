def change_working_directory(file_path):
    import os
    cwd = os.path.dirname(os.path.abspath(file_path))
    os.chdir(cwd)