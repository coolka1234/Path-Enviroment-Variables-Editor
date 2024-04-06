import os
import csv
def create_backup_log(dateOfBackup, backupPath, fileName):
    print(os.environ["BACKUPS_DIR"])
    file_path = os.path.join(os.environ["BACKUPS_DIR"],r"backup_log.csv")
    print(file_path)
    with open(file_path, 'a', newline='') as file:
        writer= csv.writer(file)
        writer.writerow([dateOfBackup, backupPath, fileName])
        file.close()
def create_log_dict(dateOfBackup, backupPath, fileName):
    log_dict = {
        "date_of_backup": dateOfBackup,
        "backup_path": backupPath,
        "name_of_backup": fileName,
    }
    return log_dict