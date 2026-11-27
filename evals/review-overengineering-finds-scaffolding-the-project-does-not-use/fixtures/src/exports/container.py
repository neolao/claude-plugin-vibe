from exports.csv_exporter import CsvExporter


class Container:
    def __init__(self):
        self._factories = {}

    def register(self, key, factory):
        self._factories[key] = factory

    def resolve(self, key):
        return self._factories[key]()


def build_container():
    container = Container()
    container.register("exporter", CsvExporter)
    return container
