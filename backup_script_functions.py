import os
import shutil
import subprocess
import datetime
import time
def createEnviromentalVariable(name="BACKUPS_DIR", value=None):
    value = os.path.expanduser(r"~")
    value=os.path.join(value, "backups")
    os.environ[name] = value
    print(f"Environmental variable {name} set to {value}")

def copyFiles(source, destination, backupName):
    subprocess.run(["robocopy", source, destination, "/E"])
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
                os.rename(os.path.join(root, name), new_file_path+f"_{id_counter}")
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
                os.rename(os.path.join(root, name), new_dir_path+f"_{id_counter}")
                id_counter += 1


def backup_catalog(pathOfFileToBackup, newBackupPath=None):
    if newBackupPath is not None:
        createEnviromentalVariable(name="BACKUPS_DIR", value=newBackupPath)
    copyFiles(pathOfFileToBackup, os.environ["BACKUPS_DIR"])
    deleteFolder(pathOfFileToBackup)
    print("Backup completed")