"""Process entry point: `catalog-api import <feed.yaml>` loads a supplier feed."""
import click

from .feeds import load_feed


@click.group()
def main() -> None:
    pass


@main.command("import")
@click.argument("feed", type=click.Path(exists=True))
def import_feed(feed: str) -> None:
    products = load_feed(feed)
    click.echo(f"{len(products)} products imported")
