# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    def __init__(self, n = "", fc = "", a = 0, ff = "") -> None:
        self.name = n
        self.fur_color = fc
        self.age = a
        self.favorite_food = ff
        self.fetch_count = 0

    def __str__(self) -> str:
        """Return a string representation of a dog"""
        return f"{self.name}'s fur color is {self.fur_color}, {self.name}'s age is {self.age}, {self.name}'s favorite food is {self.favorite_food}, and {self.name}'s fetch count is {self.fetch_count}"
    
mydog = Dog("logan", "black", 7, "salmon")
chrisdog = Dog("luna", "black and white", 6, "tortillas")

print(chrisdog)
