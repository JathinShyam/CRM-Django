from django.test import TestCase, Client
from django.urls import reverse
from App.models import *
import json
from django.contrib.auth.models import User



class TestView(TestCase):

    def setUp(self):

        self.client = Client()
        self.home_url = reverse('home')
        self.register_user_url = reverse('register')
        self.logout_url = reverse('logout')
        self.customer_record_url = reverse('customer_record', args=[1])
        self.delete_customer_url = reverse('delete_customer', args=[1])
        self.add_customer_url = reverse('add_customer')
        self.update_customer_url = reverse('update_customer', args=[1])
        self.send_email_url = reverse('send_email')
        self.import_csv_url = reverse('import_csv')
        self.search_results_url = reverse('search_results')
        self.submit_query_url = reverse('submit_query')
        self.view_queries_url = reverse('view_queries')
        self.assign_employee_url = reverse('assign_employee')

        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_register_user_GET(self):
        response = self.client.get(self.register_user_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_logout_user_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 302)
        # self.assertRedirects(response, '/')
        self.assertTemplateNotUsed(response, 'home.html')

    
  

"""

    def test_customer_record_authenticated(self):
            # Log in the user
            self.client.login(username='testuser', password='password')

            # Send a GET request to the customer record page
            response = self.client.get(self.customer_record_url)

            # Check that the response status code is 200 for authenticated user
            self.assertEquals(response.status_code, 200)

            # Check that the correct template is used for rendering
            self.assertTemplateUsed(response, 'customer.html')

            # Check that the context contains the customer record
            self.assertEqual(response.context['customer_record'], self.customer)

    def test_customer_record_GET(self):
            response = self.client.get(self.customer_record_url)

            self.assertEquals(response.status_code, 302)
            self.assertRedirects(response, '/')
            self.assertTemplateUsed(response, 'customer_record.html')
  

    def test_customer_record_GET_authenticated(self):
        # Log in a user (assuming you have a user to log in)
        self.client.login(username='jathinshyam', password='1102')

        response = self.client.get(self.customer_record_url)

        # Check that the response status code is 200 for authenticated user
        self.assertEquals(response.status_code, 302)

        # Check that the correct template is used for rendering
        self.assertTemplateUsed(response, 'customer.html')

    def test_customer_record_GET_unauthenticated(self):
        response = self.client.get(self.customer_record_url)

        # Check that the response status code is 302 for unauthenticated user
        self.assertEquals(response.status_code, 302)

        # Check that the user is redirected to the home page (change '/' to the actual URL)
        self.assertRedirects(response, 'home.html')




    
    def test_delete_customer_GET(self):
        response = self.client.get(self.delete_customer_url)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertTemplateNotUsed(response, 'delete_customer.html')

    def test_add_customer_GET(self):
        response = self.client.get(self.add_customer_url)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'add_customer.html')

    def test_update_customer_GET(self):
        response = self.client.get(self.update_customer_url)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'update_customer.html')
    
    def test_send_email_GET(self):
        response = self.client.get(self.send_email_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'send_email.html')

    def test_import_csv_GET(self):
        response = self.client.get(self.import_csv_url)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'import_csv.html')
    
    def test_search_results_GET(self):
        response = self.client.get(self.search_results_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')
    
    def test_submit_query_GET(self):
        response = self.client.get(self.submit_query_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_query.html')
    
    def test_view_queries_GET(self):
        response = self.client.get(self.view_queries_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_queries.html')
    
    def test_assign_employee_GET(self):
        response = self.client.get(self.assign_employee_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'assign_employee.html')
    
    # def test_home_POST(self):
    #     response = self.client.post(self.home_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'home.html')

    # def test_register_user_POST(self):
    #     response = self.client.post(self.register_user_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'register.html')

    # def test_logout_user_POST(self):
    #     response = self.client.post(self.logout_url)

    #     self.assertEquals(response.status_code, 302)
    #     self.assertRedirects(response, '/')
    #     self.assertTemplateNotUsed(response, 'logout.html')

    # def test_customer_record_POST(self):
    #     response = self.client.post(self.customer_record_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'customer_record.html')
    
    # def test_delete_customer_POST(self):
    #     response = self.client.post(self.delete_customer_url)

    #     self.assertEquals(response.status_code, 302)
    #     self.assertRedirects(response, '/')
    #     self.assertTemplateNotUsed(response, 'delete_customer.html')
    
    # def test_add_customer_POST(self):
    #     response = self.client.post(self.add_customer_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'add_customer.html')
    
    # def test_update_customer_POST(self):
    #     response = self.client.post(self.update_customer_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'update_customer.html')
    
    # def test_send_email_POST(self):
    #     response = self.client.post(self.send_email_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'send_email.html')
    
    # def test_import_csv_POST(self):
    #     response = self.client.post(self.import_csv_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'import_csv.html')
    
    # def test_search_results_POST(self):
    #     response = self.client.post(self.search_results_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'search_results.html')
    
    # def test_submit_query_POST(self):
    #     response = self.client.post(self.submit_query_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'submit_query.html')

    # def test_view_queries_POST(self):
    #     response = self.client.post(self.view_queries_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'view_queries.html')
    
    # def test_assign_employee_POST(self):
    #     response = self.client.post(self.assign_employee_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'assign_employee.html')"""