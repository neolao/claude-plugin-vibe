"""Process entry point: wires the modules, then serves."""

from orders.promotions import configure_promotions


def load_promotions():
    return []


def serve():
    pass


def main():
    configure_promotions(load_promotions())
    serve()


if __name__ == "__main__":
    main()
