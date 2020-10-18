from datetime import date


class Book:
    loan_duration = 14  # days

    def __init__(self, title, series, author):
        self._title = title
        self._series = series
        self._author = author
        self._checked_out_on = None

    def checkout(self, checked_out_on=date.today()):
        """
        Method to checkout a book.
        """
        self._checked_out_on = checked_out_on

    def is_overdue(self):
        """
        Method to check if a book is overdue.
        """
        overdue = False

        if self._checked_out_on is not None:
            elapsed_days = (date.today() - self._checked_out_on).days
            overdue = elapsed_days > self.loan_duration

        return overdue

    def __repr__(self):
        return f"{self._title} by {self._author}"

    @classmethod
    def create_series(cls, series, author, *args):
        """
        Factory class method for creating a series of books.
        """
        return [cls(title, series, author) for title in args]

    @staticmethod
    def get_titles(*args):
        """
        Static method that accepts a variable number
        of Book instances and returns a list of their titles.
        """
        return [book._title for book in args]


# Call class method to create a series of books.
lord_of_the_rings = Book.create_series(
    "The Lord of the Rings",
    "J.R.R. Tolkien",
    "The Fellowship of the Ring",
    "The Two Towers",
    "The Return of the King")

print(lord_of_the_rings)
# [The Fellowship of the Ring by J.R.R. Tolkien, The Two Towers by J.R.R. Tolkien, The Return of the King by J.R.R. Tolkien]

# Unpack the lord_of_the_rings list into the individual books.
fellowship_of_the_ring, two_towers, return_of_the_king = lord_of_the_rings

print(fellowship_of_the_ring)  # The Fellowship of the Ring by J.R.R. Tolkien
print(two_towers)  # The Two Towers by J.R.R. Tolkien
print(return_of_the_king)  # The Return of the King by J.R.R. Tolkien

# Call the static `Book.getTitles()` method
# to get a list of the book titles.
book_titles = Book.get_titles(
    fellowship_of_the_ring,
    two_towers,
    return_of_the_king)

print(", ".join(book_titles))
# The Fellowship of the Ring, The Two Towers, The Return of the King

# Checkout the first book in the series.
fellowship_of_the_ring.checkout(
    checked_out_on=date.fromisoformat("2020-04-01"))

# Check to see if any of the books are overdue.
print(fellowship_of_the_ring.is_overdue())  # True <-- today's date is at least 14 days past 2020-04-01
print(two_towers.is_overdue())  # False
print(return_of_the_king.is_overdue())  # False
