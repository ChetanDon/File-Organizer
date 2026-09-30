import unittest
import os
import shutil
from organizer.health import check_disk_usage

class TestFileOrganizer(unittest.TestCase):
    def test_disk_usage(self):
        metrics = check_disk_usage()
        self.assertIn("percent_used", metrics)
        self.assertGreater(metrics["total_gb"], 0)

if __name__ == "__main__":
    unittest.main()