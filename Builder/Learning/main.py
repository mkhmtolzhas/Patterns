from abc import ABC, abstractmethod
from typing import Any

class Car:
    def __init__(self):
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Car parts: {[part for part in self.parts]}")


class Builder(ABC):
    @property
    @abstractmethod
    def car(self) -> Car:
        pass

    @abstractmethod
    def set_seats(self, seats: int) -> None:
        pass

    @abstractmethod
    def set_engine(self, engine: str) -> None:
        pass

    @abstractmethod
    def set_gps(self) -> None:
        pass

    

class CarBuilder(Builder):
    def __init__(self):
        self.reset()

    @property
    def car(self) -> Car:
        car = self._car
        self.reset()
        return car

    def reset(self) -> None:
        self._car = Car()

    def set_seats(self, seats: int = 4) -> None:
        self._car.add({seats})

    def set_engine(self, engine: str = "Standart Engine") -> None:
        self._car.add({engine})

    def set_gps(self) -> None:
        self._car.add({"gps": "added"})




class Director:
    def __init__(self):
        self._builder = None
    

    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder
    
    def build_standart_car(self) -> None:
        self._builder.set_seats()
        self._builder.set_engine()
        self._builder.set_gps()



if __name__ == "__main__":
    director = Director()
    builder = CarBuilder()
    director.builder = builder

    director.build_standart_car()
    builder.car.list_parts()


    print("Custom: ")
    builder.set_engine("Olzhas")
    builder.set_gps()
    builder.set_seats(5)
    builder.car.list_parts()