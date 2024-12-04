from pathlib import Path
import pygetwindow as gw
import yaml

def get_window_pos(application: str):
    app_windows = gw.getWindowsWithTitle(application)
    app_window = app_windows[0]
    
    return app_window.topleft


def get_window_size(application: str):
    app_window = gw.getWindowsWithTitle(application)[0]
    return app_window.size


def get_window_names(config):
    return config["names"]


def update_app_vars(config, application: str) -> None:
    app_x, app_y = get_window_pos(application=application)
    app_width, app_height = get_window_size(application=application)
    
    config["window_positions"][application]["position"]["x"] = app_x
    config["window_positions"][application]["position"]["y"] = app_y
    config["window_positions"][application]["position"]["width"] = app_width
    config["window_positions"][application]["position"]["height"] = app_height


def update_all_app_vars(config):
    apps = get_window_names(config)
    for app in apps:
        update_app_vars(config, app)

    config_path = Path(__file__).parent.parent / "config" / "config.yaml"
    with open(config_path, "w") as file:
        yaml.dump(config, file, default_flow_style=False)


if __name__ == "__main__":
    # This block is for testing purposes
    from utils.config_loader import load_config

    config = load_config()
    print(update_all_app_vars(config))
