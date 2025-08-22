from abc import ABC, abstractmethod

class IEmailAnalyzer(ABC):

    @abstractmethod
    def analyse_email(self, email_content: str) -> tuple:
        """
        Analyses the given email content and returns a tuple containing two elements:
        The first element is the category of the email, which can be either "Produtivo" or "Improdutivo".
        The second element is a list of suggestions for the user to improve the email content.

        Args:
            email_content (str): The content of the email to analyze

        Returns:
            tuple: A tuple containing the category and the suggestions for improving the email content
        """
        pass
