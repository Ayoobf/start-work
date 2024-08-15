import os
import time
import logging
from pywinauto import Desktop
from .utils.config_loader import load_config

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
        return False

    try:
        command = f'start "" "{path}"'
        if args:
            command += f" {args}"
        logger.debug(f"Executing command: {command}")
        os.system(command)
        logger.info(f"Launched: {path}")
        return True
    except Exception as e:
        logger.error(f"Failed to launch {path}. Error: {str(e)}", exc_info=True)
        return False


def launch_teams(config):
    return launch_application(
        config["paths"]["teams"], "Teams", '--processStart "Teams.exe"'
    )


def launch_outlook(config):
    return launch_application(config["paths"]["outlook"], "Outlook")


def launch_edge(config):
    return launch_application(config["paths"]["edge"], "Edge")


def launch_all_applications(config):
    logger.info("Starting to launch all applications")
    apps_launched = False

    apps_launched |= launch_teams(config)
    logger.debug("Waiting 2 seconds after launching Teams")
    time.sleep(2)  # Give Teams a moment to start

    apps_launched |= launch_outlook(config)
    apps_launched |= launch_edge(config)

    logger.info("Finished launching all applications")
    return apps_launched


if __name__ == "__main__":
    # This block is for testing purposes
    from src.utils.config_loader import load_config

    config = load_config()
    launch_all_applications(config)
