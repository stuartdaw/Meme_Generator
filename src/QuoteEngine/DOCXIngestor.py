from typing import List
import docx
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class DOCXIngestor(IngestorInterface):
    """ Class to ingest DOCX files """

    allowed_doc_types = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Overrides abstract class method for docx files"""

        if not cls.can_ingest(path):
            raise f"Can't ingest {path}. Not a valid DOCX file."

        quotes = []
        wd_doc = docx.Document(path)

        for line in wd_doc.paragraphs:
            if line.text != "":
                parse = line.text.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
