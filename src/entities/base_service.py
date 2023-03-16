from abc import ABC, abstractmethod


class BaseService(ABC):
    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def select(self) -> dict:
        pass

    @abstractmethod
    def insert(self, body: dict) -> dict:
        pass

    @abstractmethod
    def update(self, field_id: int, body: dict) -> dict:
        pass

    @abstractmethod
    def delete(self, field_id: int) -> dict:
        pass
