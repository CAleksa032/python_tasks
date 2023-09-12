import random


class CandyMan:
    def __init__(self):
        self.count = 0
        self.size = 0
        self.red = 0

    def add_candy(self, size, is_red):
        self.count += 1
        self.size += size
        if is_red:
            self.red += 1

    def get_a_random_candy(self):
        size = random.randint(1, 10)
        is_red = random.choice([True, False])
        return size, is_red

    def get_average_size(self):
        if self.count == 0:
            return 0
        return self.size / self.count

    def get_red_candy_chance(self):
        if self.count == 0:
            return 0
        return self.red / self.count


candy_man = CandyMan()
for _ in range(100):
    size, is_red = candy_man.get_a_random_candy()
    candy_man.add_candy(size, is_red)

print("Average Size:", candy_man.get_average_size())
print("Red Candy Chance:", "{:.1f}".format(candy_man.get_red_candy_chance()*100), '%')
