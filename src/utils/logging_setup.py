import logging
import os


def setup_logger(config):
    logger = logging.getLogger("start_work")
    log_level = getattr(logging, config["logging"]["level"].upper())
    logger.setLevel(log_level)

    log_dir = os.path.dirname(config["logging"]["file"])
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    file_handler = logging.FileHandler(config["logging"]["file"])
    file_handler.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
