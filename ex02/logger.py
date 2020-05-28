import time
import getpass
from random import randint


def log(func):
    def wrapper_log(*args, **kwargs):
        t1 = time.perf_counter()
        ret = func(*args, **kwargs)
        totalTime = time.perf_counter() - t1
        unit = "s" if totalTime >= 1.0 else "ms"
        if unit == "ms":
            totalTime *= 1000
        name = func.__name__.replace("_", " ").title()
        with open("machine.log", "a") as ml:
            print("({})Running: {:20} [ exec-time = {:.3f} {:2} ]"
                  .format(getpass.getuser(), name, totalTime, unit), file=ml)
        return ret
    return wrapper_log


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
            self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
