import json
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add src to path so we can import lambda_function
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    @patch('lambda_function.s3_client')
    @patch('lambda_function.get_claude_summary')
    def test_successful_summarization(self, mock_summary, mock_s3):
        """Test that lambda processes S3 file and saves summary"""

        # Fake S3 event — simulates file upload trigger
        fake_event = {
            'Records': [{
                's3': {
                    'bucket': {'name': 'test-bucket'},
                    'object': {'key': 'documents/test.txt'}
                }
            }]
        }

        # Mock S3 returning file content
        mock_s3.get_object.return_value = {
            'Body': MagicMock(read=lambda: b'This is a test document about cloud engineering in Canada.')
        }

        # Mock Claude returning a summary
        mock_summary.return_value = "This document discusses cloud engineering roles in Canada."

        # Run the lambda
        result = lambda_handler(fake_event, None)

        # Check it worked
        self.assertEqual(result['statusCode'], 200)
        body = json.loads(result['body'])
        self.assertEqual(body['message'], 'Document summarized successfully')
        print("Test passed — Lambda processed document successfully")

    @patch('lambda_function.s3_client')
    def test_error_handling(self, mock_s3):
        """Test that lambda handles errors gracefully"""

        fake_event = {
            'Records': [{
                's3': {
                    'bucket': {'name': 'test-bucket'},
                    'object': {'key': 'documents/test.txt'}
                }
            }]
        }

        # Simulate S3 error
        mock_s3.get_object.side_effect = Exception("S3 bucket not found")

        result = lambda_handler(fake_event, None)

        self.assertEqual(result['statusCode'], 500)
        print("Test passed — Lambda handled error gracefully")

if __name__ == '__main__':
    unittest.main()