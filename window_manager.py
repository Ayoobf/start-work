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
        logger.info(f"{edge_window} is maximized")
        return

    logger.info(f"{edge_window} is not maximized. Maximizing now!")
    edge_window.moveTo(900, 100)  # move to first monitor
    edge_window.maximize()


def mov_outlook_window():
    try:
        outlook_windows = gw.getWindowsWithTitle("outlook")
        outlook_window = outlook_windows[0]

        if len(outlook_windows) == 0:
            logger.warning("outlook was not running")
            return

        # Wierd behavior seen here. Basically we need to resize small then snap to left then resize to desired size again
        outlook_window.resizeTo(300, 200)
        outlook_window.moveTo(-967, 394)
        outlook_window.resizeTo(974, 1080)
        return

    except Exception as e:
        logger.error(e)


def mov_teams_window():
    pass


def mov_all_windows():
    pass


if __name__ == "__main__":
    mov_outlook_window()
    print(mov_outlook_window())
