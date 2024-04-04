import os
import subprocess
import backup_script_functions as bsf
import datetime
import sys
def backup_catalog(pathOfFileToBackup, newBackupPath=None, nameOfBackup=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+"backup.zip"):
    if newBackupPath is not None:
        bsf.createEnviromentalVariable(name="BACKUPS_DIR", value=None)
    else :
        bsf.createEnviromentalVariable(value=None)
    subprocess.run(["powershell", "Compress-Archive", ".\\empty_folder", os.environ["BACKUPS_DIR"] + nameOfBackup], check=True)
    bsf.copyFiles(pathOfFileToBackup, os.environ["BACKUPS_DIR"]+ nameOfBackup, nameOfBackup)

if __name__ == "__main__":
    backup_catalog(pathOfFileToBackup=os.path.normpath(sys.argv[1]), newBackupPath=".\\backups")