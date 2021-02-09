from django.test import TestCase

from example.core.models import Book


class AssertQuerySetEqualTests(TestCase):
    def test_comparison(self):
        Book.objects.create(title="Meditations")
        Book.objects.create(title="Antifragile")

        self.assertQuerysetEqual(
            Book.objects.order_by("title"),
            ["<Book: Antifragile>", "<Book: Meditations>"],
        )
