from app.api.decorators.exception import ServiceError
import nltk
import ssl

def download_nltk_data():
    """
    Download the required NLTK data packages.

    This function is a wrapper around the NLTK library's download functionality.
    It downloads the required packages and handles any exceptions that may occur
    during the download process.

    The packages downloaded are:
    - Punkt Tokenizer Models
    - Stopwords
    - RSLP Stemmer
    - Punkt Tokenizer Models for Portuguese

    The function raises a ServiceError if any of the downloads fail.
    """
    try:
        _create_unverified_https_context = ssl._create_unverified_context
        ssl._create_default_https_context = _create_unverified_https_context
    except AttributeError:
        pass

    resources = {
        'punkt': 'tokenizers/punkt',
        'stopwords': 'corpora/stopwords',
        'rslp': 'stemmers/rslp',
        'punkt_tab': 'tokenizers/punkt_tab/portuguese'
    }

    for resource, path in resources.items():
        try:
            nltk.data.find(path)
        except LookupError:
            try:
                nltk.download(resource)
            except Exception as e:
                raise ServiceError(f"Erro ao baixar {resource}: {e}")


