from operator import le
import os
import subprocess
import backup_script_functions as bsf
import datetime
import sys
import create_backup_log as cbl
def backup_catalog(pathOfFileToBackup,namesSignature, newBackupPath=None, nameOfBackup=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+"backup.zip"):
    if newBackupPath is not None:
        bsf.createEnviromentalVariable(name="BACKUPS_DIR", value=newBackupPath)
    else :
        bsf.createEnviromentalVariable(value=None)
    if not os.path.exists(os.environ["BACKUPS_DIR"]):
        os.mkdir(os.environ["BACKUPS_DIR"])
    subprocess.run(["powershell","mkdir", (nameOfBackup)])
    bsf.copyFiles(pathOfFileToBackup, nameOfBackup, nameOfBackup, namesSignature=namesSignature)
    cbl.create_backup_log(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"),os.path.join(os.environ["BACKUPS_DIR"], nameOfBackup), nameOfBackup)
    subprocess.run(["powershell", "Compress-Archive", nameOfBackup,os.path.join(os.environ["BACKUPS_DIR"], nameOfBackup), "-Force"], check=True)
    bsf.deleteFolder(nameOfBackup)

if __name__ == "__main__":
    namesSignature = True
    backupPath=".\\backups\\"
    nameOfBackup = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+"backup.zip"
    try:
        if(len(sys.argv) ==5):
            if(sys.argv[4] == "-n"):
                namesSignature = False
            backup_catalog(pathOfFileToBackup=os.path.normpath(sys.argv[2]), newBackupPath=os.path.normpath(sys.argv[1]), namesSignature=namesSignature, nameOfBackup=sys.argv[3])
        elif(len(sys.argv) == 4) and (sys.argv[3] == "-n"):
            namesSignature = False
            backup_catalog(pathOfFileToBackup=sys.argv[1], newBackupPath=backupPath, namesSignature=namesSignature, nameOfBackup=sys.argv[2])
        elif(len(sys.argv) == 3):
            backup_catalog(pathOfFileToBackup=os.path.normpath(sys.argv[1]), newBackupPath=backupPath, namesSignature=namesSignature, nameOfBackup=sys.argv[2])
        else:
            raise Exception("Invalid number of arguments")
    except Exception as e:
        print(e)
        print("Usage: python backup.py [newBackupPath] <pathToFileToBackup> <nameOfBackup> [-n]")
        print("newBackupPath - path to directory where backup will be stored. WARNING: upon changing of this path, old backups will be moved to a new location, and deleted from the old one.")
        print("pathToFileToBackup - path to file or directory to backup")
        print("-n - do not rename files to timestamps-name_of_backup-extension format")
        print("nameOfBackup - name of backup file")
        sys.exit(1)