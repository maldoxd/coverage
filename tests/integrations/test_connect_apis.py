import time
import unittest
from unittest.mock import patch, MagicMock

import httpx

from app.integrations.connect_apis import get_coverage_api
from app.models.api1 import API1
from app.models.coverage import Coverage

class TestConnectApis(unittest.TestCase):

    @patch('app.integrations.connect_apis.make_request')
    @patch('app.integrations.connect_apis.parse_api_response')
    def test_get_coverage_api(self, mock_parse_api_response, mock_make_request):
        api_instance = API1()
        member_id = 12345
        url = api_instance.url + str(member_id)
        mock_make_request.return_value = {'api_field1': 10, 'api_field2': 20, 'api_field3': 30}
        mock_parse_api_response.return_value = Coverage(oop_max=10, remaining_oop_max=20, copay=30)

        result = get_coverage_api(api_instance, member_id)

        mock_make_request.assert_called_once_with(url)
        mock_parse_api_response.assert_called_once_with({'api_field1': 10, 'api_field2': 20, 'api_field3': 30}, api_instance.field_mapping)
        self.assertEqual(result, Coverage(oop_max=10, remaining_oop_max=20, copay=30))

    @patch('app.integrations.connect_apis.make_request')
    @patch('app.integrations.connect_apis.parse_api_response')
    def test_get_coverage_api_retry(self, mock_parse_api_response, mock_make_request):
        api_instance = API1()
        member_id = 12345
        url = api_instance.url + str(member_id)
        mock_make_request.side_effect = [httpx.RequestError("An error occurred"), {'api_field1': 10, 'api_field2': 20, 'api_field3': 30}]
        mock_parse_api_response.return_value = Coverage(oop_max=10, remaining_oop_max=20, copay=30)

        result = get_coverage_api(api_instance, member_id)

        mock_make_request.assert_called_with(url)
        mock_parse_api_response.assert_called_once_with({'api_field1': 10, 'api_field2': 20, 'api_field3': 30}, api_instance.field_mapping)
        self.assertEqual(result, Coverage(oop_max=10, remaining_oop_max=20, copay=30))
        self.assertEqual(mock_make_request.call_count, 2)
        self.assertEqual(mock_parse_api_response.call_count, 1)

if __name__ == '__main__':
    unittest.main()
    