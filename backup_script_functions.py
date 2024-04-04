import os
import subprocess
def createEnviromentalVariable(name="BACKUPS_DIR", value=None):
    if value is None:
        value = os.path.expanduser(r"~\\backups")
    os.environ[name] = value
    print(f"Environmental variable {name} set to {value}")

def copyFiles(source, destination):
    subprocess.run(["robocopy", source, destination, "/E"])
    print(f"Files copied from {source} to {destination}")

def deleteFiles(path):
    subprocess.run(["rmdir", path, "/s", "/q"])
    print(f"Files deleted from {path}")

def backup_catalog(pathOfFileToBackup, newBackupPath=None):
    if newBackupPath is not None:
        createEnviromentalVariable(name="BACKUPS_DIR", value=newBackupPath)
    copyFiles(pathOfFileToBackup, os.environ["BACKUPS_DIR"])
    deleteFiles(pathOfFileToBackup)
    print("Backup completed")