from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import pandas as pd


class TXTIngestor(IngestorInterface):
    """ Class to ingest TXT files """

    allowed_doc_types = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Overrides abstract class method for txt files"""

        if not cls.can_ingest(path):
            raise f"Can't ingest {path}. Not a valid TXT file."

        quotes = []

        with open(path, 'r') as f:
            lines = f.readlines()

        counter = True
        for line in lines:
            # Always a special character added to 1st line. This removes it
            if counter:
                counter = False
                details = line.split('-')
                quotes.append(QuoteModel(details[0][1:].strip('\r\n'), details[1].strip('\r\n')))
            else:
                details = line.split('-')
                quotes.append(QuoteModel(details[0].strip('\r\n'), details[1].strip('\r\n')))

        return quotes