import os

def get_files_info(working_directory, directory=None):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    
    if os.path.commonpath([working_directory, full_path]) != working_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = []

        for name in os.listdir(full_path):
            file_path = os.path.join(full_path, name)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            files_info.append(
                f"- {name}: file_size={file_size} bytes, is_dir={is_dir}"
            )

        if files_info == []:
            return ""
        else: return '\n'.join(files_info)

    except Exception as e:
        return f'Error: {str(e)}'