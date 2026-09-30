import shutil

def check_disk_usage(path="."):
    """Checks disk usage and returns usage metrics."""
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100
    return {
        "total_gb": round(total / (1024**3), 2),
        "used_gb": round(used / (1024**3), 2),
        "free_gb": round(free / (1024**3), 2),
        "percent_used": round(percent_used, 2)
    }