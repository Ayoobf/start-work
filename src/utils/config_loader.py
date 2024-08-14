import yaml
from pathlib import Path
from typing import Dict, Any


def load_config(config_path: str = None) -> Dict[str, Any]:
    if config_path is None:
        config_path = Path(__file__).parent.parent.parent / "config" / "config.yaml"
    else:
        config_path = Path(config_path)

    if not config_path.is_file():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    resolve_references(config)
    return config


def resolve_references(config: Dict[str, Any]) -> None:
    for key, value in config.items():
        if isinstance(value, dict):
            resolve_references(value)
        elif isinstance(value, str) and value.startswith("${") and value.endswith("}"):
            ref_path = value[2:-1].split(".")
            try:
                config[key] = get_nested_value(config, ref_path)
            except KeyError:
                print(
                    f"Warning: Reference '{value}' could not be resolved. Keeping original value."
                )


def get_nested_value(config: Dict[str, Any], path: list) -> Any:
    for key in path:
        if key not in config:
            raise KeyError(f"Key '{key}' not found in configuration")
        config = config[key]
    return config


if __name__ == "__main__":
    config = load_config()
    print(yaml.dump(config, default_flow_style=False))
