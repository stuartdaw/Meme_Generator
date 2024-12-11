class QuoteModel:
    """Simple class to encapsulate body and author of a quote"""

    def __init__(self, quote: str, author: str):
        self.quote = quote.strip()
        self.author = author.strip()

    def __str__(self):
        """Return a string representation of the quote"""
        return f'"{self.quote}" - {self.author}'

    def __repr__(self):
        """Return a string representation of the quote"""
        return f'Quote:"{self.quote}", Auth:{self.author}'