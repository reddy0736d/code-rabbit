import logging
import os
from datetime import datetime
import inspect


class AutoLogger:
    """
    Centralized logging system that automatically detects the calling file name
    and creates logs with the format: filename.log
    """
    
    _loggers = {}  # Store created loggers to avoid duplicates
    
    @staticmethod
    def get_logger():
        """
        Get logger automatically based on the calling file name
        Returns logger with filename-based log file (e.g., settings.log, Issues.log)
        """
        # Get the caller's frame to determine the file name
        # Go up 2 levels to get the actual calling file (skip get_logger function call)
        frame = inspect.currentframe().f_back.f_back
        if frame is None:
            frame = inspect.currentframe().f_back
        caller_file = frame.f_code.co_filename
        
        # Extract just the filename without extension
        filename = os.path.splitext(os.path.basename(caller_file))[0]
        
        # Return existing logger if already created for this file
        if filename in AutoLogger._loggers:
            return AutoLogger._loggers[filename]
        
        # Create logs directory if it doesn't exist
        logs_dir = "./logs"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        
        # Create log filename with timestamp for uniqueness but keep main name
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_filename = os.path.join(logs_dir, f"{filename}_{timestamp}.log")
        
        # Create logger
        logger = logging.getLogger(filename)
        logger.setLevel(logging.INFO)
        
        # Clear any existing handlers to avoid duplicates
        logger.handlers.clear()
        
        # Create file handler
        file_handler = logging.FileHandler(log_filename, mode="a", encoding="utf-8")
        
        # Create console handler
        console_handler = logging.StreamHandler()
        
        # Create formatter
        formatter = logging.Formatter(
            f"%(asctime)s | %(levelname)s | {filename} | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        # Apply formatter to handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        # Store logger for reuse
        AutoLogger._loggers[filename] = logger
        
        # Log the initialization
        logger.info(f"Logger initialized for {filename}.py - Log file: {log_filename}")
        
        return logger
    
    @staticmethod
    def get_custom_logger(name):
        """
        Get logger with custom name instead of auto-detecting filename
        """
        if name in AutoLogger._loggers:
            return AutoLogger._loggers[name]
        
        # Create logs directory if it doesn't exist
        logs_dir = "./logs"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        
        # Create log filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_filename = os.path.join(logs_dir, f"{name}_{timestamp}.log")
        
        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        
        # Clear any existing handlers
        logger.handlers.clear()
        
        # Create handlers
        file_handler = logging.FileHandler(log_filename, mode="a", encoding="utf-8")
        console_handler = logging.StreamHandler()
        
        # Create formatter
        formatter = logging.Formatter(
            f"%(asctime)s | %(levelname)s | {name} | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        # Apply formatter
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        # Store logger
        AutoLogger._loggers[name] = logger
        
        logger.info(f"Custom logger initialized for {name} - Log file: {log_filename}")
        
        return logger


# Convenience function for easy import
def get_logger():
    """Get automatic logger based on calling file name"""
    return AutoLogger.get_logger()


def get_custom_logger(name):
    """Get logger with custom name"""
    return AutoLogger.get_custom_logger(name)


# Example usage:
if __name__ == "__main__":
    # This will create logger_config_TIMESTAMP.log
    logger = get_logger()
    logger.info("Testing the automatic logging system")
    logger.debug("This is a debug message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")