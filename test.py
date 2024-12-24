class House:
    houses_history = []  # Список для хранения названий домов

    def __new__(cls, *args, **kwargs):
        # Получаем имя дома из первых аргументов
        house_name = args[0]
        instance = super().__new__(cls)
        cls.houses_history.append(house_name)

        return instance

    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def __del__(self):
        print(f"{self.first} снесён, но он останется в истории")


# Создание нескольких объектов класса House
h1 = House('ЖК Эльбрус', 10, 0)
print(House.houses_history)

h2 = House('ЖК Акация', 20,0 )
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20, 0)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# Удаляем оставшийся объект
del h1