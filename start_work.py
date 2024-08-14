import logging
import os
import config
from application_launcher import launch_all_applications
from window_manager import mov_all_windows
from youtube_controller import open_youtube
import time


def setup_logger():
    logger = logging.getLogger("start_work")

    # Set the log level from config
    log_level = getattr(logging, config.LOG_LEVEL.upper())
    logger.setLevel(log_level)

    # Create log directory if it doesn't exist
    log_dir = os.path.dirname(config.LOG_FILE)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create file handler which logs even debug messages
    fh = logging.FileHandler(config.LOG_FILE)
    fh.setLevel(log_level)

    # Create console handler with the same log level
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


# Set up the logger
logger = setup_logger()

if __name__ == "__main__":
    logger.info("Start Work script initiated")
    launch_all_applications()
    time.sleep(20)
    mov_all_windows()
    time.sleep(2)
    open_youtube()
    logger.info("Start Work script completed")
