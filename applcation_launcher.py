import config
import os
import time
import logging


def setup_logger():
    logger = logging.getLogger("application_launcher")

    log_level = getattr(logging, config.LOG_LEVEL.upper())
    logger.setLevel(log_level)

    # create log file
    log_dir = os.path.dirname(config.LOG_FILE)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # create file handler
    fh = logging.FileHandler(config.LOG_FILE)
    fh.setLevel(log_level)

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


logger = setup_logger()


def launch_application(path: str, args: str = None):
    try:
        command = f'start "" "{path}"'
        if args:
            command += f" {args}"
        logger.debug(f"Executing command: {command}")
        os.system(command)
        logger.info(f"Launched: {path}")
    except Exception as e:
        logger.error(f"Failed to launch {path}. Error: {str(e)}", exc_info=True)


def launch_teams():
    launch_application(config.TEAMS_UPDATE_PATH, '--processStart "Teams.exe"')


def launch_outlook():
    launch_application(config.OUTLOOK_PATH)


def launch_edge():
    launch_application(config.EDGE_PATH)


def launch_all_applications():
    logger.info("Starting to launch all applications")
    launch_teams()
    logger.debug("Waiting 2 seconds after launching Teams")
    time.sleep(2)  # Give Teams a moment to start
    launch_outlook()
    launch_edge()
    logger.info("Finished launching all applications")


if __name__ == "__main__":
    logger.info("Script started")
    launch_all_applications()
    logger.info("Script finished")
