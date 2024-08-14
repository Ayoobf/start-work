import pygetwindow as gw
import logging

logger = logging.getLogger("start_work")


def mov_edge_window():
    edge_windows = gw.getWindowsWithTitle("edge")
    edge_window = edge_windows[0]

    if len(edge_windows) == 0:
        logger.warning("edge was not running")
        return

    if edge_window.isMaximized:
        logger.info("edge is maximized")
        return

    logger.info("edge is not maximized. resizing now")
    edge_window.moveTo(900, 100)  # move to first monitor
    edge_window.maximize()
    logger.info("edge has been resized")


def mov_outlook_window():
    try:
        outlook_windows = gw.getWindowsWithTitle("outlook")
        outlook_window = outlook_windows[0]

        if len(outlook_windows) == 0:
            logger.warning("outlook was not running")
            return

        # Weird behavior seen here. Basically we need to resize small then snap to left then resize to desired size again
        outlook_window.resizeTo(300, 200)
        outlook_window.moveTo(-967, 394)
        outlook_window.resizeTo(974, 1087)
        logger.info("outlook has been resized.")

    except Exception:
        logger.warning("outlook was not running")


def mov_teams_window():
    try:
        teams_windows = gw.getWindowsWithTitle("teams")
        teams_window = teams_windows[0]

        if len(teams_windows) == 0:
            logger.warning("teams was not running")
            return

        # Weird behavior seen here. Basically we need to resize small then snap to left then resize to desired size again
        teams_window.resizeTo(300, 200)
        teams_window.moveTo(-1927, 394)
        teams_window.resizeTo(974, 1087)
        logger.info("teams has been resized.")

    except Exception:
        logger.warning("teams was not running")


def mov_all_windows():
    mov_edge_window()
    mov_outlook_window()
    mov_teams_window()


if __name__ == "__main__":
    mov_all_windows()
