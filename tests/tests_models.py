from django.test import TestCase
from restaurant.models import Booking, Menu
from datetime import datetime
import pytz
from decimal import Decimal

class BookingModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        t1 = datetime.strptime('2023-01-28 18:05:00', '%Y-%m-%d %H:%M:%S')
        london_timezone = pytz.timezone('Europe/London')
        booking_date = london_timezone.localize(t1)
        cls.booking = Booking.objects.create(
            Name = 'Paul Murphy',
            No_of_Guests = 6,
            BookingDate = booking_date
        )


    def test_fields(self):
        self.assertIsInstance(self.booking.Name, str)
        self.assertIsInstance(self.booking.No_of_Guests, int)
        self.assertIsInstance(self.booking.BookingDate,  datetime)



class MenuModelTest(TestCase):

    def setUp(self):
        Menu.objects.create(
            Title = 'Vanilla IceCream',
            Price = 6.99,
            Inventory = 99
        )

    def test_fields(self):
        vanilla = Menu.objects.get(Title='Vanilla IceCream')
        self.assertEqual(vanilla.Price, Decimal('6.99'))
        self.assertEqual(vanilla.Inventory, 99)

