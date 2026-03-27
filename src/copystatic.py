import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    to_path = dest_dir_path
    from_path = source_dir_path
    for file in os.listdir(from_path):
        from_file_path = os.path.join(from_path, file)
        to_file_path = os.path.join(to_path, file)
        if os.path.isdir(from_file_path):
            if not os.path.exists(to_file_path):
                os.mkdir(to_file_path)
            copy_files_recursive(from_file_path, to_file_path)
        else:
            shutil.copy(from_file_path, to_file_path)
