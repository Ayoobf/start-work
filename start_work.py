import time
from src.utils.config_loader import load_config
from src.application_launcher import launch_all_applications
from src.window_manager import mov_all_windows
from src.youtube_controller import open_youtube
from src.utils.logging_setup import setup_logger
from src.utils.batch_handler import move_batch_file


def main():
    config = load_config()
    logger = setup_logger(config)
    move_batch_file()

    time.sleep(config["delays"]["launch"])
    logger.info("Start Work script initiated")
    launch_all_applications(config)
    time.sleep(config["delays"]["setup"])
    mov_all_windows()
    time.sleep(2)
    open_youtube(config)
    logger.info("Start Work script completed")


if __name__ == "__main__":
    main()
