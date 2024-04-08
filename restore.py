from math import e
import os
import subprocess
import csv
import sys
import backup_script_functions as bsf
def restore(path=os.path.join(os.getcwd(), ".backups")):
    if(path=='' or path==None):
        path=os.path.join(os.getcwd(), ".backups")
    if(not os.path.exists(path) or not os.path.isdir(path)):
        print("Path does not exist or is not a directory. Creating now.")
        os.mkdir(path)
    bsf.createEnviromentalVariable(name="BACKUPS_DIR", value=None)
    #wybierz wersje
    print("Choose the version of backup to restore bu inputing which version by number:")
    backup_log_path = os.path.join(os.environ["BACKUPS_DIR"], "backup_log.csv")
    i=1
    with open(backup_log_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{i}. {row}")
            i+=1
    file.close()
    index = int(input())
    i=1
    pathOfArchive= ""
    with open(backup_log_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if(i==index):
                pathOfArchive=row[1]
                break
            i+=1
    file.close()
    #to juz rozpakowywanie
    subprocess.run(["powershell", "Expand-Archive","-Force",pathOfArchive, path])
    print("Archive unpacked successfully")
if __name__ == "__main__":
    try:
        if(len(sys.argv)<=1):
            restore()
        else:
            restore(sys.argv[1])
    except Exception as e:
        print(e)
        print("Usage: python restore.py [pathToBackupDirectory]")
        print("pathToBackupDirectory - path to directory where backup is stored")
        sys.exit(1)


