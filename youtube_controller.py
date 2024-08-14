from typing import Optional
import config
import webbrowser
import logging

logger = logging.getLogger("start_work")


def open_youtube(playlist_url: Optional[str] = None) -> None:
    """
    Opens YouTube with the specified playlist or a default one.

    Args:
        playlist_url (Optional[str]): The URL of the playlist to open. If None, uses the config URL.
    """
    url = playlist_url or config.YOUTUBE_PLAYLIST_URL
    logger.info(f"Opening YouTube playlist: {url}")
    go_to_URL(url)


def go_to_URL(url: str) -> bool:
    """
    Attempts to open the specified URL in the default web browser.

    Args:
        url (str): The URL to open.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        success = webbrowser.open(url)
        if success:
            logger.info(f"Successfully opened URL: {url}")
        else:
            logger.warning(f"Failed to open URL: {url}")
        return success
    except Exception as e:
        logger.error(f"Error opening URL {url}: {str(e)}", exc_info=True)
        return False


if __name__ == "__main__":
    open_youtube()
