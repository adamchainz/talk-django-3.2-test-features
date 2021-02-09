from django.test import TestCase

from example.core.models import Book


class AssertQuerySetEqualTests(TestCase):
    def test_comparison(self):
        book1 = Book.objects.create(title="Meditations")
        book2 = Book.objects.create(title="Antifragile")

        self.assertQuerysetEqual(
            Book.objects.order_by("title"),
            [book2, book1],
        )
