import os
import json
def create_backup_log(dateOfBackup, backupPath, fileName):
    file_path = os.path.join(os.environ["BACKUPS_DIR"],"/backup_log.json")
    with open(file_path, 'a') as file:
        json.dump(create_log_dict(dateOfBackup, backupPath, fileName), file)
        file.close()
def create_log_dict(dateOfBackup, backupPath, fileName):
    log_dict = {
        "date_of_backup": dateOfBackup,
        "backup_path": backupPath,
        "name_of_backup": fileName,
    }
    return log_dict