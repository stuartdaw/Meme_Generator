from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import pandas as pd


class CSVIngestor(IngestorInterface):
    """ Class to ingest CSV files """

    allowed_doc_types = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Overrides abstract class method for csv files"""
        # print(f'made it into CSV ingestor class')

        if not cls.can_ingest(path):
            raise f"Can't ingest {path}. Not a valid CSV file."

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
