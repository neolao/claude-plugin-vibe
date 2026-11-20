"""Process entry point: `invoice-worker --queue <name>` loops on the queue until stopped."""
import click

from .render import render_next


@click.command()
@click.option("--queue", required=True, help="Name of the queue to pop invoice jobs from.")
@click.option("--once", is_flag=True, help="Render one job and exit.")
def main(queue: str, once: bool) -> None:
    while True:
        rendered = render_next(queue)
        if once or not rendered:
            break


if __name__ == "__main__":
    main()
