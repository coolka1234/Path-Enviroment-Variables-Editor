import os
import subprocess
import backup_script_functions as bsf
import datetime
def backup_catalog(pathOfFileToBackup, newBackupPath=None, nameOfBackup=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+"backup.zip"):
    if newBackupPath is not None and not os.path.exists(newBackupPath):
        bsf.createEnviromentalVariable(name="BACKUPS_DIR", value=newBackupPath)
    else :
        bsf.createEnviromentalVariable(value=newBackupPath)
    subprocess.run(["powershell", "Compress-Archive", "-Path", ".\\empty_folder", newBackupPath, nameOfBackup], check=True)