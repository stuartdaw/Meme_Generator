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
        df = pd.read_csv(path, sep=" - ", header=None, names=['quote','author'], engine='python')

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['quote'], row['author'])
            quotes.append(new_quote)

        return quotes