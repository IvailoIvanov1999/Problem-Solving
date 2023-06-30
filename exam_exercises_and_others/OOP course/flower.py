class Flower:
    is_happy = False
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements

    def water(self, n):
        if n >= self.water_requirements:
            self.is_happy = True
            return self.is_happy

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        elif not self.is_happy:
            return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
