import os
import subprocess
import backup_script_functions as bsf
import datetime
import sys
def backup_catalog(pathOfFileToBackup, newBackupPath=None, nameOfBackup=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")+"backup.zip"):
    if newBackupPath is not None:
        bsf.createEnviromentalVariable(name="BACKUPS_DIR", value=None)
    else :
        bsf.createEnviromentalVariable(value=None)
    if not os.path.exists(os.environ["BACKUPS_DIR"]):
        os.mkdir(os.environ["BACKUPS_DIR"])
    subprocess.run(["powershell","mkdir", (nameOfBackup)])
    bsf.copyFiles(pathOfFileToBackup, nameOfBackup, nameOfBackup)
    bsf.renameFiles(nameOfBackup, nameOfBackup)
    subprocess.run(["powershell", "Compress-Archive", nameOfBackup,os.path.join(os.environ["BACKUPS_DIR"], nameOfBackup), "-Force"], check=True)
    bsf.deleteFolder(nameOfBackup)

if __name__ == "__main__":
    backup_catalog(pathOfFileToBackup=os.path.normpath(sys.argv[1]), newBackupPath=".\\backups\\")