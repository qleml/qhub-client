import unittest
from qhub_api.benchmarq import Benchmarq

class TestBenchmarq(unittest.TestCase):

    def test_no_job_passed(self):
        """Test that Benchmarq raises an error when no job is passed."""
        with self.assertRaises(ValueError): # context manager which expects a ValueError
            Benchmarq()

    def test_invalid_job_passed(self):
        """Test that Benchmarq raises an error when an invalid job is passed."""
        with self.assertRaises(ValueError):
            Benchmarq('string')
