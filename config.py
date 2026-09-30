import os

# Source directory to organize (change this to any test folder if needed)
TARGET_DIR = os.path.expanduser("~/Downloads")

# Category rules based on file extension
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Code": [".py", ".html", ".css", ".js"],
}

LOG_FILE = "organizer.log"