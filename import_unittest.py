import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_current_directory(self):
        """Test get_files_info with current directory"""
        result = get_files_info("calculator", ".")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_pkg_directory(self):
        """Test get_files_info with pkg subdirectory"""
        result = get_files_info("calculator", "pkg")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_system_directory(self):
        """Test get_files_info with system directory - should return error"""
        result = get_files_info("calculator", "/bin")
        self.assertIsInstance(result, str)
        self.assertIn("error", result.lower())

    def test_parent_directory(self):
        """Test get_files_info with parent directory - should return error"""
        result = get_files_info("calculator", "../")
        self.assertIsInstance(result, str)
        self.assertIn("error", result.lower())

def main():
    """Run tests directly and print results"""
    print("Testing with current directory:")
    print(get_files_info("calculator", "."))
    print("\nTesting with pkg directory:")
    print(get_files_info("calculator", "pkg"))
    print("\nTesting with system directory:")
    print(get_files_info("calculator", "/bin"))
    print("\nTesting with parent directory:")
    print(get_files_info("calculator", "../"))

if __name__ == '__main__':
    main()