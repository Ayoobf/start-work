import pygetwindow as gw
import logging

logger = logging.getLogger("start_work")


def mov_edge_window(config):
    app_h = config["window_positions"]["edge"]["position"]["height"]
    app_w = config["window_positions"]["edge"]["position"]["width"]
    app_x = config["window_positions"]["edge"]["position"]["x"]
    app_y = config["window_positions"]["edge"]["position"]["y"]
    
    edge_windows = gw.getWindowsWithTitle("edge")
    edge_window = edge_windows[0]

    if len(edge_windows) == 0:
        logger.warning("edge was not running")
        return

    if edge_window.isMaximized:
        logger.info("edge is maximized")
        return

    logger.info("edge is not maximized. resizing now")
    edge_window.resizeTo(300, 200)
    edge_window.moveTo(app_x, app_y)  # move to first monitor
    edge_window.resizeTo(app_w, app_h)
    edge_window.maximize()
    logger.info("edge has been resized")


def mov_outlook_window(config):
    app_h = config["window_positions"]["outlook"]["position"]["height"]
    app_w = config["window_positions"]["outlook"]["position"]["width"]
    app_x = config["window_positions"]["outlook"]["position"]["x"]
    app_y = config["window_positions"]["outlook"]["position"]["y"]

    try:
        outlook_windows = gw.getWindowsWithTitle("outlook")
        outlook_window = outlook_windows[0]

        if len(outlook_windows) == 0:
            logger.warning("outlook was not running")
            return

        # Weird behavior seen here. Basically we need to resize small then snap to left then resize to desired size again
        outlook_window.resizeTo(300, 200)
        outlook_window.moveTo(app_x, app_y)
        outlook_window.resizeTo(app_w, app_h)
        logger.info("outlook has been resized.")

    except Exception:
        logger.warning("outlook was not running")


def mov_teams_window(config):
    app_h = config["window_positions"]["teams"]["position"]["height"]
    app_w = config["window_positions"]["teams"]["position"]["width"]
    app_x = config["window_positions"]["teams"]["position"]["x"]
    app_y = config["window_positions"]["teams"]["position"]["y"]

    try:
        teams_windows = gw.getWindowsWithTitle("teams")
        teams_window = teams_windows[0]

        if len(teams_windows) == 0:
            logger.warning("teams was not running")
            return

        # Weird behavior seen here. Basically we need to resize small then snap to left then resize to desired size again
        teams_window.resizeTo(300, 200)
        teams_window.moveTo(app_x, app_y)
        teams_window.resizeTo(app_w, app_h)
        logger.info("teams has been resized.")

    except Exception:
        logger.warning("teams was not running")


def mov_all_windows(config):
    mov_edge_window(config)
    mov_outlook_window(config)
    mov_teams_window(config)


if __name__ == "__main__":
    from utils.config_loader import load_config
    config = load_config()
    mov_all_windows(config=config)
