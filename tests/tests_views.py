from django.test import TestCase, RequestFactory
from restaurant.models import Booking, Menu
from restaurant.views import MenuItemsView, BookingViewSet
from datetime import datetime
import pytz


class MenuItemViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(
            Title = 'Vanilla IceCream',
            Price = 6.99,
            Inventory = 99
        )

    def test_my_view(self):
        request = RequestFactory().get('Vanilla IceCream')
        view = MenuItemsView()
        view.setup(request)



class BookingViewTest(TestCase):

    def setUp(self):
        t1 = datetime.strptime('2023-01-31 19:05:00', '%Y-%m-%d %H:%M:%S')
        london_timezone = pytz.timezone('Europe/London')
        booking_date = london_timezone.localize(t1)
        Booking.objects.create(
            Name = 'Kieran Malloy',
            No_of_Guests = 4,
            BookingDate = booking_date
        )

    def test_my_view(self):
        request = RequestFactory().get('Kieran Malloy')
        view = BookingViewSet()
        view.setup(request)