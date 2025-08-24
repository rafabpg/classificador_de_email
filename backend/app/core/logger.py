import logging
import sys
from pathlib import Path
from app.core.config import settings

def setup_logger():
    """
    Configures the root logger for the application.

    Removes any existing handlers, then sets the log level to DEBUG if
    settings.DEBUG is True, otherwise sets it to INFO.

    Adds a console handler with a custom formatter and log level.

    If settings.DEBUG is False, creates a directory named "logs" if it
    doesn't exist, and adds a file handler with a custom formatter and
    log level set to INFO.

    Sets the log level for the "uvicorn", "httpx", and "httpcore" loggers
    to WARNING.

    Returns the configured logger.
    """
    logger = logging.getLogger("app")
    
    if logger.handlers:
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
    
    log_level = logging.DEBUG if settings.DEBUG else logging.INFO
    logger.setLevel(log_level)
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)
    logger.addHandler(console_handler)
    
    if not settings.DEBUG:
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)  
        logger.addHandler(file_handler)
    
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    
    return logger

logger = setup_logger()