from app.domain.useCases.analysis import AnalysisUseCase
from app.adapters.TextReaderAdapter import TextReaderAdapter
from app.domain.interfaces import ITextReaderAdapter
from app.domain.interfaces import INLPAdapter
from app.adapters.NLPAdapter import NLPAdapter
from app.domain.interfaces import IEmailAnalyzer
from app.adapters.EmailAnalyzer import EmailAnalyzer
from fastapi import Depends

def get_nlp_adapter():
    return NLPAdapter()

def get_email_analyzer():
    return EmailAnalyzer()

def get_text_reader_adapter():
    return TextReaderAdapter()

def get_analysis_use_case(text_reader_adapter: ITextReaderAdapter = Depends(get_text_reader_adapter), nlp_adapter: INLPAdapter = Depends(get_nlp_adapter), email_analyzer: IEmailAnalyzer = Depends(get_email_analyzer)):
    return AnalysisUseCase(text_reader_adapter=text_reader_adapter, nlp_adapter=nlp_adapter, email_analyzer=email_analyzer)
