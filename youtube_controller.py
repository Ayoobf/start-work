import config
import webbrowser
import logging

logger = logging.getLogger("start_work")


def open_youtube():
    logger.info("opening youtube")
    go_to_URL(config.YOUTUBE_PLAYLIST_URL)


def go_to_URL(url: str):
    try:
        webbrowser.open(url)
    except Exception:
        logger.error(f"youtube controller Error: {Exception}")


if __name__ == "__main__":
    open_youtube()
