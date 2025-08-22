from app.domain.interfaces.INLPAdapter import INLPAdapter
import re
import unicodedata
import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from nltk.tokenize import word_tokenize
from app.api.decorators.exception import ServiceError

class NLPAdapter(INLPAdapter):

    _url_pattern = re.compile(r'http\S+|www\S+|https\S+')
    _symbol_pattern = re.compile(r'[^a-z0-9áàâãéèêíïóôõöúçñ\s]')
    _number_pattern = re.compile(r'\b\d+\b')
    _space_pattern = re.compile(r'\s+')

    def __init__(self):
        self.stop_words = set(stopwords.words('portuguese'))
        self.stemmer = RSLPStemmer()

    def _remove_accents(self, text: str) -> str:
        """
        Remove accents from a given string.

        This function uses the unicodedata.normalize() function with the 'NFD'
        form to separate accents from the base letters. It then removes
        characters that are classified as 'Mn' by the unicodedata.category()
        function, which corresponds to non-spacing marks (i.e. the accents).

        Args:
            text (str): The string from which to remove the accents.

        Returns:
            str: The string without accents.
        """
        return ''.join(
            c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn'
        )

    def preprocess(self, text: str) -> str:
        if not text or not isinstance(text, str):
            raise ValueError("Texto inválido para preprocessamento.")

        text = text.lower()
        text = self._url_pattern.sub(' ', text)
        text = self._symbol_pattern.sub(' ', text)
        text = self._remove_accents(text)
        text = self._number_pattern.sub(' ', text)
        text = self._space_pattern.sub(' ', text).strip()

        try:
            tokens = word_tokenize(text, language='portuguese')
            processed_tokens = [
                self.stemmer.stem(word)
                for word in tokens
                if word not in self.stop_words and len(word) > 2
            ]
            return " ".join(processed_tokens)

        except Exception as e:
            raise ServiceError(f"Erro no processamento NLP: {e}")