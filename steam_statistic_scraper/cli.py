import click
import configparse


from getData import commands as getDataGroup
from exportData import commands as exportDataGroup

@click.group()
def cli():
    pass

@cli.command()
def main():
    """A steam statistic scraper to copy steam statistic in a local database."""
    greet = 'Hello'
    click.echo('{0}.'.format(greet))

@cli.command()
def version():
    """Display the current version."""
    click.echo(_read_version())

cli.add_command(getDataGroup.getallloggedinuserdata)
#cli.add_command(exportDataGroup.command_group)


if __name__ == '__main__':
    cli()
