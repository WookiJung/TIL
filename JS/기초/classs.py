class Car:
    def __init__(self, options):
        self.title = options.get('title')

    def drive(self):
        return '부릉부릉'


options = {'title': '세단', 'color': 'blue'}
car = Car(options)
car.title  # bmw
car.drive()  # 부릉 부릉


class Mercedes(Car):
    def __init__(self, options):
        super().__init__(options)
        self.color = options.get('color')

    def honk(self):
        return '빵빵'

    
eclass = Mercedes(options)

print(
    eclass.title,
    eclass.color,
    eclass.drive(),
    eclass.honk(),
)

