import os
import shutil
from config import FILE_CATEGORIES

def organize_folder(target_dir, logger):
    """Scans directory and moves files into extension-based subfolders."""
    if not os.path.exists(target_dir):
        logger.error(f"Directory {target_dir} does not exist.")
        return 0

    moved_count = 0
    for entry in os.scandir(target_dir):
        if entry.is_file():
            file_ext = os.path.splitext(entry.name)[1].lower()
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(target_dir, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    dest_path = os.path.join(dest_folder, entry.name)
                    
                    try:
                        shutil.move(entry.path, dest_path)
                        logger.info(f"Moved: {entry.name} -> {category}/")
                        moved_count += 1
                    except Exception as e:
                        logger.error(f"Failed to move {entry.name}: {e}")
                    break
    return moved_count