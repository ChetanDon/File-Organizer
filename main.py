from config import TARGET_DIR
from utils.logger import setup_logger
from organizer.sorter import organize_folder
from organizer.health import check_disk_usage

def main():
    logger = setup_logger()
    logger.info("Starting File Organizer process.")
    print("=== File Organizer & System Health Utility ===")
    
    # 1. Health Monitor
    metrics = check_disk_usage()
    print(f"[Health Check] Disk Usage: {metrics['percent_used']}% "
          f"({metrics['free_gb']} GB Free / {metrics['total_gb']} GB Total)")
    
    # 2. File Organization
    print(f"[Sorting] Organizing directory: {TARGET_DIR}")
    files_moved = organize_folder(TARGET_DIR, logger)
    print(f"[Complete] Successfully organized {files_moved} file(s).")
    print("Logs written to organizer.log")

if __name__ == "__main__":
    main()