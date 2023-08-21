import unittest
import requests

# Service name is used by the test container
DEV_URL = "http://weather_app:5000"

# This URL is used when tests have to be run locally
LOCAL_URL = "http://0.0.0.0:80"

session = requests.Session()

class TestSum(unittest.TestCase):
    def test_web_server_running(self, url=DEV_URL):
        resp = requests.get(url, timeout=5)
        result = False
        if resp.status_code == 200:
            result = True
        else:
            result = False
        self.assertTrue(result, True)

    def test_post_running(self, url=DEV_URL):
        cookies = {
            'session': 'eyJ1cGxvYWRlZF9kYXRhX2ZpbGVfcGF0aCI6InN0YXRpY0ZpbGVzL3VwbG9hZHMvbW9jay5jc3YifQ.ZOK7uQ.tQ4UHAmHaxqplDv9z510_-tRf_E',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryRA213vAhfYmwBORB',
            'Cookie': 'session=eyJ1cGxvYWRlZF9kYXRhX2ZpbGVfcGF0aCI6InN0YXRpY0ZpbGVzL3VwbG9hZHMvbW9jay5jc3YifQ.ZOK7uQ.tQ4UHAmHaxqplDv9z510_-tRf_E',
        }

        data = '------WebKitFormBoundaryRA213vAhfYmwBORB\r\nContent-Disposition: form-data; name="file"; filename="mock.csv"\r\nContent-Type: text/csv\r\n\r\n\r\n------WebKitFormBoundaryRA213vAhfYmwBORB--\r\n'

        resp = requests.post(url, cookies=cookies, headers=headers, data=data)
        result = False
        if resp.status_code == 200:
            result = True
        else:
            result = False
        self.assertTrue(result, True)

    '''
    def test_web_server_limit(self, url="http://127.0.0.1/query"):
        cookies = {
            'session': 'eyJ1cGxvYWRlZF9kYXRhX2ZpbGVfcGF0aCI6InN0YXRpY0ZpbGVzL3VwbG9hZHMvbW9jay5jc3YifQ.ZN5bOw.xg-0h4TGWZHfRRYYlvebfK0V6PM',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Connection': 'keep-alive',
            'Cookie': 'session=eyJ1cGxvYWRlZF9kYXRhX2ZpbGVfcGF0aCI6InN0YXRpY0ZpbGVzL3VwbG9hZHMvbW9jay5jc3YifQ.ZN5bOw.xg-0h4TGWZHfRRYYlvebfK0V6PM',
        }

        params = {
            'limit': '1',
        }

        resp = requests.get(url, params=params, cookies=cookies, headers=headers)
        
        result = False
        if resp.status_code == 200:
            result = True
        else:
            result = False

        resp_txt = resp.text
        python_dict = json.loads(resp_txt)
        limit_count = 0

        if "date" in python_dict:
            limit_count += 1
        self.assertTrue(result, True)
    '''
if __name__ == '__main__':
    unittest.main()
