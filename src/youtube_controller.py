import webbrowser
import logging
import random

logger = logging.getLogger("start_work")


def open_youtube(config):
    logger.info("Opening YouTube")
    playlist_url = get_playlist_url(config)
    go_to_URL(playlist_url)


def get_playlist_url(config):
    if config["features"]["use_random_playlist"]:
        playlists = config["youtube"]["alternative_playlists"]
        playlists.append(config["youtube"]["playlist_url"])
        return random.choice(playlists)
    else:
        return config["youtube"]["playlist_url"]


def go_to_URL(url: str):
    try:
        webbrowser.open(url)
        logger.info(f"Opened URL: {url}")
    except Exception as e:
        logger.error(f"YouTube controller Error: {str(e)}", exc_info=True)


if __name__ == "__main__":
    # This block is for testing purposes
    from utils.config_loader import load_config

    config = load_config()
    open_youtube(config)
