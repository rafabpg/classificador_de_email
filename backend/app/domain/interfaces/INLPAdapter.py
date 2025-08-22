from abc import ABC, abstractmethod

class INLPAdapter(ABC):

    @abstractmethod
    def preprocess(self, text: str) -> str:
        """
        Preprocesses a given text by performing the following steps:
        1. Remove accents;
        2. Remove URLs;
        3. Remove symbols;
        4. Remove numbers;
        5. Remove extra spaces;
        6. Tokenize the text;
        7. Remove stopwords;
        8. Apply stemming to the tokens;
        9. Join the tokens back into a string;
        """
       
        pass