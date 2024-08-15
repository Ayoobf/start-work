import os
import shutil as process
import logging
import getpass

logger = logging.getLogger(__name__)


def move_batch_file():
    # Get the current user's username
    username = getpass.getuser()

    # Construct the correct path to the Startup folder
    STARTUP_PATH = f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/start_work.bat"

    try:
        # Check if the source batch file exists
        if not os.path.exists("start_work.bat"):
            raise FileNotFoundError("start_work.bat not found in the current directory")

        # Copy the batch file to the Startup folder
        process.copy("start_work.bat", STARTUP_PATH)
        logger.info(f"Successfully copied start_work.bat to {STARTUP_PATH}")
    except FileNotFoundError as e:
        logger.error(f"Error: {str(e)}")
    except PermissionError:
        logger.error("Permission denied when trying to write to the Startup folder")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    # Set up basic logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    move_batch_file()
