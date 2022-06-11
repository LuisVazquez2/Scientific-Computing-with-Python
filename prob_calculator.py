import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        else:
            return_list = []
            for i in range(number):
                return_list.append(self.contents.pop(
                    random.randint(0, len(self.contents)-1)))
            return return_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    for i in range(num_experiments):
        temp = copy.deepcopy(hat)
        x = temp.draw(num_balls_drawn)
        x = {i: x.count(i) for i in x}
        flag = True
        for key, value in expected_balls.items():
            if key not in x:
                flag = False
            elif value > x[key]:
                flag = False
        if flag:
            #print(f"{x}   :  {expected_balls}")
            probability += 1
    return probability/num_experiments
    

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=10)
actual = probability
expected = 0.272
print("Actual:", actual)