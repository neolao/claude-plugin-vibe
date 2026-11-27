from abc import ABC, abstractmethod


class OrderRepository(ABC):
    @abstractmethod
    def shipped_on(self, day):
        raise NotImplementedError
