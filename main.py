from rename_wizard.counter.renamer_counter import RenamerCounter
from rename_wizard.directory_renamer import DirectoryRenamer
from rename_wizard.renamer import Renamer
from rename_wizard.cli.rename_wizard_cli import RenameWizardCli

file_renamer: DirectoryRenamer = DirectoryRenamer()
renamer: Renamer = Renamer(file_renamer)
renamer_counter: RenamerCounter = RenamerCounter()
cli = RenameWizardCli(renamer, renamer_counter).load_commands()

if __name__ == "__main__":
    cli()
