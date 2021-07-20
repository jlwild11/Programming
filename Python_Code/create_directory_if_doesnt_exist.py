def create_directory_if_doesnt_exist(directory):
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)
        