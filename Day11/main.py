class Monkey:
    def __init__(self, items, operator, second, test, true, false):
        self.items = items
        self.operation = operator
        self.second = second
        self.test = test
        self.true = true
        self.false = false
        self.inspected = 0

    def __repr__(self):
        out = ""
        for i in self.items:
            out += str(i) + ' '
        return out


class MonkeyFactory:
    def __init__(self, path):
        self.__path = path
        self.many_lines = {}
        self.readfile()

    def readfile(self):
        file_in = open(self.__path)
        one_line = file_in.readlines()
        self.many_lines = [i.strip().removesuffix('\n') for i in one_line]

    def do_monkeys(self) -> list:
        monkeys = []
        for i in range(0, len(self.many_lines)-1, 7):
            items = [int(item.removesuffix(',')) for item in self.many_lines[i+1].split(' ')[2:]]
            operation = self.many_lines[i+2].split(' ')[4]
            second = self.many_lines[i+2].split(' ')[5]
            test = int(self.many_lines[i + 3].split(' ')[3])
            true = int(self.many_lines[i + 4].split(' ')[5])
            false = int(self.many_lines[i + 5].split(' ')[5])
            monkey = Monkey(items, operation, second, test, true, false)
            monkeys.append(monkey)
        return monkeys;


class ThrowItems:
    def __init__(self, monkeys):
        self.monkeys = monkeys
        self.mult = 1
        for monkey in monkeys:
            self.mult *= monkey.test
        for i in range(10000):
            self.throw()

    def __repr__(self):
        out = ""
        for i in self.monkeys:
            out += str(i.inspected) + ' '
        return out

    def __str__(self):
        out = ""
        for i in self.monkeys:
            out += str(i.inspected) + ' '
        return out

    def throw(self):
        for monkey in self.monkeys:
            for item in monkey.items:
                monkey.inspected += 1
                if monkey.second == 'old':
                    second = item
                else:
                    second = int(monkey.second)
                if monkey.operation == '*':
                    item = item * second
                else:
                    item = item + second
                iter = item//self.mult
                item = item-self.mult*iter
                if item%monkey.test == 0:
                    self.monkeys[monkey.true].items.append(item)
                else:
                    self.monkeys[monkey.false].items.append(item)
            monkey.items.clear()

    def monkey_business(self):
        inspector = [monkey.inspected for monkey in self.monkeys]
        max1 = max(inspector)
        inspector.remove(max1)
        max2 = max(inspector)
        return max1*max2


factory = MonkeyFactory('input.txt')
myMonkeys = factory.do_monkeys()
throwing = ThrowItems(myMonkeys)
print(throwing.monkey_business())
