import os
from typing import Annotated

import typer
from rich import print
from rich.table import Table

from rename_wizard.enum.casing_type_enum import CasingTypeEnum
from rename_wizard.counter.renamer_counter import RenamerCounter
from rename_wizard.renamer import Renamer


class RenameWizardCli:
    __renamer: Renamer
    __renamer_counter: RenamerCounter

    def __init__(self, renamer: Renamer, renamer_counter: RenamerCounter):
        self.__renamer = renamer
        self.__renamer_counter = renamer_counter

    def load_commands(self):
        app = typer.Typer()

        @app.command()
        def hello():
            print("Hello there ! Thank you for installing RenameWizard !")

        @app.command()
        def rename_my_directories(
            target_directory_path: Annotated[
                str,
                typer.Argument(help="The folder path from which you want to start the renaming from"),
            ]
        ):
            print("\n[bold cyan]Here are the possible conventions for renaming your directories.[/bold cyan]\n\n")

            table = Table(title="Convention examples")
            table.add_column("Convention Name", justify="left", style="cyan", no_wrap=True)
            table.add_column("Original Directory", justify="left", style="white")
            table.add_column("Renamed Directory", justify="left", style="white")

            table.add_row("snake_case", "ThisIsanexample.txt", "this_is_an_example.txt")
            table.add_row("kebab_case", "ThisIsanexample.txt", "this-is-an-example.txt")
            table.add_row("camel_case", "ThisIsanexample.txt", "thisIsAnExample.txt")
            table.add_row("pascal_case", "ThisIsanexample.txt", "ThisIsAnExample.txt")

            print(table)

            casing_type: str = typer.prompt("\nPlease choose the convention you want: ")

            while casing_type not in [item.value for item in CasingTypeEnum]:
                print("\n:x: [bold]The chosen convention is not one of the available conventions.[/bold] (Spelling counts).")
                casing_type: CasingTypeEnum = typer.prompt("\nPlease choose the convention you want: ")

            absolute_path: str = os.path.abspath(target_directory_path)
            self.__renamer_counter.count_directories(target_directory_path)
            self.__renamer.rename(absolute_path, casing_type)

            print(f"\n:white_check_mark: It's done ! We renamed {self.__renamer_counter.directory_counter} directories.\n\n")

        return app()
