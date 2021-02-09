from django.test import TestCase

from example.core.models import Book


class SetUpTestDataTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title="Meditations")

    def test_that_changes_title(self):
        self.book.title = "Antifragile"

    def test_that_reads_title_from_db(self):
        db_title = Book.objects.get().title
        assert db_title == "Meditations"

    def test_that_reads_in_memory_title(self):
        assert self.book.title == "Meditations"
