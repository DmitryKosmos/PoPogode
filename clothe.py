class Clothe():
    def __init__(self, name, type, temp_min, temp_max, delt):
        self.name = name
        self.type = type
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.delt = delt

##вершки
futbolka = Clothe("Футболка", "body_top", 17, 100, 5)
fufaika = Clothe("Кофта", "body_top", 10, 17, 10)
sviter = Clothe("Свитер", "body_top", 0, 17, 15)
hudi = Clothe("Худи", "body_top", 0, 17, 15)
vetrovka = Clothe("Ветровка", "body_top2", 0, 15, 20)
kurtka = Clothe("Куртка", "body_top2", 0, 17, 25)

##корешки
shorti = Clothe("Шорты","legs", 17, 100, 5)
treniki = Clothe("Спортивки","legs", 10, 30, 10)
jins = Clothe("Джинсы","legs", 0, 25, 15)
termo = Clothe("Подштанники","legs", -10, 5, 15)

##допы
umbrella = Clothe("Зонт","rain", (), (), ())

##print(umbrella.temp_min)
