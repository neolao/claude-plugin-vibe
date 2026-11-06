"""Process entry point: builds the dispatcher, then serves."""

from shop.dispatch import Dispatcher
from shop.handlers import billing, shipping


def serve(dispatcher):
    pass


def main():
    dispatcher = Dispatcher({"billing": billing.handle, "shipping": shipping.handle})
    serve(dispatcher)


if __name__ == "__main__":
    main()
