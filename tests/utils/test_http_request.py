import unittest

from app.models.coverage import Coverage
from app.utils.http_request import parse_api_response

class TestHttpRequest(unittest.TestCase):
    def test_parse_api_response(self):
        api_response = {
            'api_field1': 10,
            'api_field2': 20,
            'api_field3': 30
        }
        field_mapping = {
            'api_field1': 'oop_max',
            'api_field2': 'remaining_oop_max',
            'api_field3': 'copay'
        }
        expected_result = Coverage(oop_max=10, remaining_oop_max=20, copay=30)
        
        result = parse_api_response(api_response, field_mapping)
        self.assertEqual(result, expected_result)
    
    def test_parse_api_response_missing_field(self):
        api_response = {
            'api_field1': 10,
            'api_field3': 30
        }
        field_mapping = {
            'api_field1': 'oop_max',
            'api_field2': 'remaining_oop_max',
            'api_field3': 'copay'
        }
        expected_result = Coverage(oop_max=10, remaining_oop_max=0, copay=30)
        
        result = parse_api_response(api_response, field_mapping)
        self.assertEqual(result, expected_result)
    
    def test_parse_api_response_empty_response(self):
        api_response = {}
        field_mapping = {
            'api_field1': 'oop_max',
            'api_field2': 'remaining_oop_max',
            'api_field3': 'copay'
        }
        expected_result = Coverage(oop_max=0, remaining_oop_max=0, copay=0)
        
        result = parse_api_response(api_response, field_mapping)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()