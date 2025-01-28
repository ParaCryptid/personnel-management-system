
import unittest
from app import app

class PersonnelManagementTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Personnel Management System", response.get_json()["message"])

    def test_analyze_employee_data(self):
        employee_data = {
            "employee_data": [
                {"name": "John", "age": 30, "department": "HR", "salary": 50000},
                {"name": "Jane", "age": 35, "department": "IT", "salary": 70000}
            ]
        }
        response = self.app.post('/analyze_employee_data', json=employee_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("employee_analysis", response.get_json())

    def test_analyze_sentiment(self):
        feedback = {"feedback": "The work environment is very positive and motivating."}
        response = self.app.post('/analyze_sentiment', json=feedback)
        self.assertEqual(response.status_code, 200)
        self.assertIn("analysis", response.get_json())

    def test_secure_employee_data(self):
        secure_data_request = {"data": "Confidential information"}
        response = self.app.post('/secure_employee_data', json=secure_data_request)
        self.assertEqual(response.status_code, 200)
        self.assertIn("encrypted_data", response.get_json())

if __name__ == '__main__':
    unittest.main()
