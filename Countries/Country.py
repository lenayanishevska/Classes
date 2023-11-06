
class Country:
    def __init__(self, name: str, population: int):
        self.__name = name
        self.__population = population

    def add(self, other_country):
        new_name = f"{self.__name} {other_country.__name}"
        new_population = self.__population + other_country.__population
        return Country(new_name, new_population)

    def __add__(self, other):
        new_name = f"{self.__name} {other.__name}"
        new_population = self.__population + other.__population
        return Country(new_name, new_population)

    def __str__(self):
        output = f"Country name: {self.__name} \nCountry population: {self.__population}"
        return output
