import unittest
from api.datatypes import Sample

class TestSample(unittest.TestCase):
    def test_example(self):
        sample_record = Sample().get_sample(6009)
        print(sample_record)
        assert True

if __name__ == '__main__':
    unittest.main()
