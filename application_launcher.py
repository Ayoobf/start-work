import config
import os
import time
import logging
from pywinauto import Desktop

logger = logging.getLogger("start_work")


def is_process_running(process_name):
    try:
        windows = Desktop(backend="uia").windows()
        for window in windows:
            window_text = window.window_text()
            logger.debug(f"Found window: {window_text}")
            if process_name.lower() in window_text.lower():
                logger.info(f"Process {process_name} is already running")
                return True
        logger.info(f"Process {process_name} is not running")
        return False
    except Exception as e:
        logger.error(
            f"Error checking if {process_name} is running: {str(e)}", exc_info=True
        )
        return False


def launch_application(path: str, process_name: str, args: str = None):
    if is_process_running(process_name):
        logger.info(f"{process_name} is already running. Skipping launch.")
        return

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
    launch_application(config.TEAMS_UPDATE_PATH, "Teams", '--processStart "Teams.exe"')


def launch_outlook():
    launch_application(config.OUTLOOK_PATH, "Outlook")


def launch_edge():
    launch_application(config.EDGE_PATH, "Edge")


def launch_all_applications():
    logger.info("Starting to launch all applications")
    launch_teams()
    logger.debug("Waiting 2 seconds after launching Teams")
    time.sleep(2)  # Give Teams a moment to start
    launch_outlook()
    launch_edge()
    logger.info("Finished launching all applications")
