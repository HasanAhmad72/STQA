import os
import unittest

from create_excel import generate_sample_data
from student_filter import analyze_student_marks


class TestStudentFilter(unittest.TestCase):
    TEST_FILE = "test_students.xlsx"

    @classmethod
    def setUpClass(cls):
        # Setup test spreadsheet prior to testing
        generate_sample_data(cls.TEST_FILE)

    @classmethod
    def tearDownClass(cls):
        # Clean up created file after testing
        if os.path.exists(cls.TEST_FILE):
            os.remove(cls.TEST_FILE)

    def test_sample_data_counts(self):
        """Black-Box Test: Verify counts match calculated expected values."""
        any_count, all_count = analyze_student_marks(self.TEST_FILE)

        # Expected from sample data:
        # Any > 60: Amit, Neha, Raj, Sneha, Pooja, Rohan, Kiran = 7
        # All > 60: Amit, Sneha, Rohan, Kiran = 4
        self.assertEqual(any_count, 7, "Count for ANY subject > 60 is incorrect")
        self.assertEqual(all_count, 4, "Count for ALL subjects > 60 is incorrect")

    def test_file_not_found_exception(self):
        """White-Box Test: Verify exception handling when file does not exist."""
        with self.assertRaises(FileNotFoundError):
            analyze_student_marks("non_existent_file.xlsx")


if __name__ == "__main__":
    unittest.main()
