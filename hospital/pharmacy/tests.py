# tests.py
from django.test import TestCase
from graphene.test import Client
from .schema import schema
from .models import Customer, Order
from .utils import send_sms
from django.utils import timezone

class GraphQLTests(TestCase):
    def setUp(self):
        self.client = Client(schema)

    def test_query_all_customers(self):
        response = self.client.execute('''{
            allCustomers {
                id
                name
            }
        }''')
        self.assertIsNone(response.get('errors'))
        # Add more assertions as needed
    
    def test_mutation_add_order(self):
        response = self.client.execute('''
            mutation {
                addOrder(orderData: {
                    customerCode: "123",
                    item: "Test Item",
                    amount: 100
                }) {
                    order {
                        id
                        customer {
                            id
                        }
                        item
                    }
                }
            }
        ''')
        self.assertIsNone(response.get('errors'))
        # Add more assertions as needed

    def test_mutation_add_customer(self):
        response = self.client.execute('''
            mutation {
                addCustomer(customerData: {
                    name: "Test Customer",
                    code: "123",
                    phoneNumber: "1234567890"
                }) {
                    customer {
                        id
                        name
                    }
                }
            }
        ''')
        self.assertIsNone(response.get('errors'))
        # Add more assertions as needed

    # Add more test cases as needed

class TestUtils(TestCase):
    def test_send_sms(self):
        # Mocking the send_sms function and test its behavior
        pass
