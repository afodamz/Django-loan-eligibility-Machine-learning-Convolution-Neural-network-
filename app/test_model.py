from django.test import TestCase

# Create your tests here.
from app.models import UserLoan


# class UserLoanTestCase(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass
#
#     def setUp(self):
#         UserLoan.objects.create(name="lion", sound="roar")
#         UserLoan.objects.create(name="cat", sound="meow")
#
#     def test_email_can_speak(self):
#         user1 = UserLoan.objects.get(name="lion")
#         user2 = UserLoan.objects.get(name="cat")
#         self.assertEqual(user1.Email, 'anyname@gmail.com')
#         self.assertEqual(user2.Email, 'anyname2@gmail.com')
#
#     def test_first_name_label(self):
#         loan = UserLoan.objects.get(id=1)
#         field_label = loan._meta.get_field('first_name').verbose_name
#         self.assertEqual(field_label, 'first name')

