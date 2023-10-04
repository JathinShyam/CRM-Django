from django.test import SimpleTestCase
from django.urls import reverse, resolve
from App.views import home, logout_user, register_user, customer_record, delete_customer, add_customer, update_customer, send_email, import_csv, search_results, submit_query, assign_employee, view_queries


class TestUrls(SimpleTestCase):

    def test_home_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
    
    def test_logout_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_user)

    def test_register_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_user)
    
    def test_customer_record_is_resolved(self):
        url = reverse('customer_record', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, customer_record)
    
    def test_delete_customer_is_resolved(self):
        url = reverse('delete_customer', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_customer)

    def test_add_customer_is_resolved(self):
        url = reverse('add_customer')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_customer)

    def test_update_customer_is_resolved(self):
        url = reverse('update_customer', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, update_customer)
    
    def test_send_email_is_resolved(self):
        url = reverse('send_email')
        print(resolve(url))
        self.assertEquals(resolve(url).func, send_email)

    def test_import_csv_is_resolved(self):
        url = reverse('import_csv')
        print(resolve(url))
        self.assertEquals(resolve(url).func, import_csv)

    def test_search_results_is_resolved(self):
        url = reverse('search_results')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search_results)
    
    def test_submit_query_is_resolved(self):
        url = reverse('submit_query')
        print(resolve(url))
        self.assertEquals(resolve(url).func, submit_query)

    def test_view_queries_is_resolved(self):
        url = reverse('view_queries')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_queries)

    def test_assign_employee_is_resolved(self):
        url = reverse('assign_employee')
        print(resolve(url))
        self.assertEquals(resolve(url).func, assign_employee)