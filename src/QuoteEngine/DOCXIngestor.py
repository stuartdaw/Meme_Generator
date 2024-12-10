from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import pandas as pd


class DOCXIngestor(IngestorInterface):
    """ Class to ingest DOCX files """

    allowed_doc_types = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Overrides abstract class method for docx files"""

        if not cls.can_ingest(path):
            raise (f"Can't ingest {path}. Not a valid DOCX file.")

        quotes = []
        df = pd.read_csv(path, sep=" - ", header=None, names=['quote','author'])

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['quote'], row['author'])
            quotes.append(new_quote)

        return quotes