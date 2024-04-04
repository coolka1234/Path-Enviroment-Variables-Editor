import os
import subprocess
import datetime
import time
def createEnviromentalVariable(name="BACKUPS_DIR", value=None):
    if value is None:
        value = os.path.expanduser(r"~")
        value+=r"\backups"
    os.environ[name] = value
    print(f"Environmental variable {name} set to {value}")

def copyFiles(source, destination, backupName):
    subprocess.run(["robocopy", source, destination, "/E"])
    renameFiles(destination, datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+"-"+backupName)
    print(f"Files copied from {source} to {destination}")

def deleteFiles(path):
    subprocess.run(["rmdir", path, "/s", "/q"])
    print(f"Files deleted from {path}")
def renameFiles(path, backupName):
    for file in os.listdir(path):
        time_of_file = os.path.getmtime(os.path.join(path, file))
        time_of_file_str = time.strftime('%Y_%m_%d_%H_%M_%S', time.gmtime(time_of_file))
        file_name, file_extension = os.path.splitext(file)
        try:
            os.rename(os.path.join(path, file), os.path.join(time_of_file_str,backupName, file_extension))
        except FileNotFoundError:
            print(f"File {file} from {path} not found")
def backup_catalog(pathOfFileToBackup, newBackupPath=None):
    if newBackupPath is not None:
        createEnviromentalVariable(name="BACKUPS_DIR", value=newBackupPath)
    copyFiles(pathOfFileToBackup, os.environ["BACKUPS_DIR"])
    deleteFiles(pathOfFileToBackup)
    print("Backup completed")