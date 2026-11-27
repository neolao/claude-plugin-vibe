from abc import ABC, abstractmethod


class OrderRepository(ABC):
    @abstractmethod
    def add(self, order):
        raise NotImplementedError
