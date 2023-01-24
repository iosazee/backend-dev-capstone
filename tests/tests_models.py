from django.test import TestCase
from restaurant.models import Booking, Menu
from datetime import datetime
from decimal import Decimal

class BookingModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.booking = Booking.objects.create(
            Name = 'Paul Murphy',
            No_of_Guests = 6,
        )

    def test_fields(self):
        self.assertIsInstance(self.booking.Name, str)
        self.assertIsInstance(self.booking.No_of_Guests, int)

    def test_timestamps(self):
        self.assertIsInstance(self.booking.BookingDate, datetime)


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

