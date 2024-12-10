class QuoteModel:
    """Simple class to encapsulate body and author of a quote"""

    def __init__(self, quote: str, author: str):
        self.quote = quote
        self.author = author

    def __str__(self):
        """Return a string representation of the quote"""
        return f'Quote: "{self.quote}"- By: {self.author}'

    def __repr__(self):
        """Return a string representation of the quote"""
        return f'Q:{self.quote}, Auth: {self.author}'