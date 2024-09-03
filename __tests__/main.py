import unittest


loader = unittest.TestLoader()
suite = loader.discover(start_dir='./__tests__/', pattern='test_*.py')
runner = unittest.TextTestRunner()

if __name__ == "__main__":
    runner.run(suite)
