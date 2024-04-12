import unittest

from unittest.mock import patch

from fastapi import HTTPException
from app.api.member_coverage import coalesce_coverages, coalesce
from app.models.coverage import Coverage

class TestMemberCoverage(unittest.TestCase):
    @patch('app.api.member_coverage.get_coverage')
    def test_coalesce_coverages(self, mock_get_coverage):
        # Mock the get_coverage function to return a list of coverages
        mock_get_coverage.return_value = [
            Coverage(oop_max=10, remaining_oop_max=20, copay=30),
            Coverage(oop_max=15, remaining_oop_max=25, copay=35),
            Coverage(oop_max=10, remaining_oop_max=20, copay=30)
        ]
        
        expected_result = Coverage(oop_max=10, remaining_oop_max=20, copay=30)
        
        result = coalesce_coverages(123)
        
        self.assertEqual(result, expected_result)
    
    @patch('app.api.member_coverage.get_coverage')
    def test_coalesce_coverages_member_not_found(self, mock_get_coverage):
        # Mock the get_coverage function to return an empty list
        mock_get_coverage.return_value = []
        
        with self.assertRaises(HTTPException) as cm:
            coalesce_coverages(123)
        
        self.assertEqual(cm.exception.status_code, 404)
        self.assertEqual(cm.exception.detail, "Member not found")
    
    def test_coalesce(self):
        coverages = [
            Coverage(oop_max=10, remaining_oop_max=20, copay=30),
            Coverage(oop_max=15, remaining_oop_max=25, copay=35),
            Coverage(oop_max=10, remaining_oop_max=20, copay=30)
        ]
        
        expected_result = Coverage(oop_max=10, remaining_oop_max=20, copay=30)
        
        result = coalesce(coverages)
        
        self.assertEqual(result, expected_result)
    
    @patch('app.api.member_coverage.get_coverage')
    def test_coalesce_coverages_internal_server_error(self, mock_get_coverage):
        # Mock the get_coverage function to raise an exception
        mock_get_coverage.side_effect = Exception("API error")
        
        with self.assertRaises(HTTPException) as cm:
            coalesce_coverages(123)
        
        self.assertEqual(cm.exception.status_code, 500)
        self.assertEqual(cm.exception.detail, "Internal server error")

if __name__ == '__main__':
    unittest.main()