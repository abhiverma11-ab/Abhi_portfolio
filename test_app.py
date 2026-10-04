import unittest
from app import create_app
from database import db
from models import Project, BlogPost, ContactMessage, AdminUser

class PortfolioTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()

    def test_public_routes(self):
        routes = [
            '/',
            '/about',
            '/skills',
            '/projects',
            '/projects/studylens-ai',
            '/projects/ipl-data-analysis-dashboard',
            '/projects/ai-career-guidance',
            '/projects/train-traffic-control-ai',
            '/summer-training',
            '/experience',
            '/certifications',
            '/hackathons',
            '/resume',
            '/blog',
            '/blog/my-journey-learning-python',
            '/contact'
        ]
        for route in routes:
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200, f"Route {route} failed with status {response.status_code}")
                self.assertIn(b'Abhi', response.data)

    def test_contact_form_post(self):
        response = self.client.post('/contact', data={
            'name': 'Test Recruiter',
            'email': 'recruiter@tech.com',
            'subject': 'Internship Opportunity',
            'message': 'We would love to discuss an AI internship opportunity with you.'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thank you, your message has been received!', response.data)

        # Check DB
        with self.app.app_context():
            msg = ContactMessage.query.filter_by(email='recruiter@tech.com').first()
            self.assertIsNotNone(msg)
            self.assertEqual(msg.subject, 'Internship Opportunity')

    def test_api_contact(self):
        response = self.client.post('/api/contact', json={
            'name': 'API Tester',
            'email': 'api@test.com',
            'subject': 'API Test Subject',
            'message': 'Testing AJAX contact API'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertTrue(data['success'])

    def test_download_routes(self):
        # Test download-project
        res_proj = self.client.get('/download-project')
        self.assertIn(res_proj.status_code, [200, 302])

        # Test download-resume
        res_resume = self.client.get('/download-resume')
        self.assertIn(res_resume.status_code, [200, 302])

    def test_admin_auth_and_dashboard(self):
        # 1. Access without login -> redirects to login
        res = self.client.get('/admin/dashboard')
        self.assertEqual(res.status_code, 302)

        # 2. Login with valid credentials
        login_res = self.client.post('/admin/login', data={
            'username': 'admin',
            'password': 'admin123'
        }, follow_redirects=True)
        self.assertEqual(login_res.status_code, 200)
        self.assertIn(b'Control Dashboard', login_res.data)

        # 3. Access admin sub-pages
        admin_pages = [
            '/admin/dashboard',
            '/admin/projects',
            '/admin/blogs',
            '/admin/certificates',
            '/admin/skills',
            '/admin/messages'
        ]
        for page in admin_pages:
            with self.subTest(admin_page=page):
                res = self.client.get(page)
                self.assertEqual(res.status_code, 200, f"Admin page {page} failed")

if __name__ == '__main__':
    unittest.main()
