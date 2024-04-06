import os
from re import sub
import shutil
import subprocess
import datetime
import time
def createEnviromentalVariable(name="BACKUPS_DIR", value=None):
    if name in os.environ.keys() and value is not None:
        copyFiles(os.environ[name], value, "backup", False)
        deleteFolder(os.environ[name])
        print(f"Environmental variable {name} already exists. Deleting old folder and copying files to new location")
    if value is None:
        value = os.path.expanduser(r"~")
        value=os.path.join(value, "backups")
    os.environ[name] = value
    if "BACKUPS_DIR" in os.environ:
        print(f"Environmental variable BACKUPS_DIR set to {os.environ['BACKUPS_DIR']}")

def copyFiles(source, destination, backupName, namesSignature):
    subprocess.run(["robocopy", source, destination, "/E"])
    if namesSignature:
        renameFiles(destination, datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+"-"+backupName)
    print(f"Files copied from {source} to {destination}")

def deleteFolder(path):
    subprocess.run(["powershell", "Remove-Item", path, "-Recurse", "-Force"])

def renameFiles(path, backupName):
    id_counter = 0
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            time_of_file = os.path.getmtime(os.path.join(root, name))
            time_of_file_str = time.strftime('%Y_%m_%d_%H_%M_%S', time.gmtime(time_of_file))
            _, file_extension = os.path.splitext(name)
            new_file_name = f"{time_of_file_str}_{backupName}{file_extension}"
            new_file_path = os.path.join(root, new_file_name)
            try:
                os.rename(os.path.join(root, name), new_file_path)
            except FileNotFoundError:
                print(f"File {name} from {os.path.join(root, name)} not found")
            except FileExistsError:
                os.rename(os.path.join(root, name), insert_before_dot(new_file_path, id_counter))
                id_counter += 1
        for name in dirs:
            time_of_file = os.path.getmtime(os.path.join(root, name))
            time_of_file_str = time.strftime('%Y_%m_%d_%H_%M_%S', time.gmtime(time_of_file))
            new_dir_name = f"{time_of_file_str}_{backupName}"
            new_dir_path = os.path.join(root, new_dir_name)
            try:
                os.rename(os.path.join(root, name), new_dir_path)
            except FileNotFoundError:
                print(f"Directory {name} from {os.path.join(root, name)} not found")
            except FileExistsError:
                os.rename(os.path.join(root, name), insert_before_dot(new_dir_path, id_counter))
                id_counter += 1


def insert_before_dot(filename, string_to_insert):
    name, extension = os.path.splitext(filename)
    new_name = f"{name}_{string_to_insert}{extension}"
    return new_name