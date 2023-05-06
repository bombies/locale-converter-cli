import configparser
import typer
from pathlib import Path
from localegen import (DIR_ERROR, FILE_ERROR, SUCCESS, __app_name__)

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"


def _init_config_file() -> int:
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        typer.echo("Failed to create config directory.")
        return DIR_ERROR
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        typer.echo("Failed to create config file.")
        return FILE_ERROR
    return SUCCESS
