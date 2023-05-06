from typing import Optional
from pathlib import Path

import typer

from localegen.app import LocaleGenerator, ValidLanguage
from localegen import __app_name__, __version__

app = typer.Typer()


def get_locale_generator(path: str) -> LocaleGenerator:
    return LocaleGenerator(path)


@app.command()
def convert(
        path: str = typer.Argument(..., help="Path to the file or directory to convert."),
        language: str = typer.Option(ValidLanguage.SPANISH.value[0], "--language", "-l", help="Language to convert to."),
) -> None:
    if path is None:
        typer.echo("No path provided.")
        raise typer.Exit()
    if language is None:
        typer.echo("No language provided.")
        raise typer.Exit()

    locale_generator = get_locale_generator(path)
    typer.echo(f"Converting {path} to {language}...")
    locale_generator.generate_locale(ValidLanguage.from_str(language))
    typer.echo("Done.")


@app.command()
def convertall(
        path: str = typer.Argument(..., help="Path to the file or directory to convert.")
) -> None:
    locale_generator = get_locale_generator(path)
    for language in ValidLanguage:
        typer.echo(f"Converting {path} to {language}...")
        locale_generator.generate_locale(language)
    typer.echo("Done.")

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    return
