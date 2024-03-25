class CustomSet:
    def __init__(self):
        self.list = []

    def add(self, item):
        if item not in self.list:
            self.list.append(item)

    def remove(self, item):
        try:
            if item in self.list:
                self.list.remove(item)
        except KeyError:
            print("Item not removed, moving forward")

    def as_list(self):
        return self.list

    def clear(self):
        self.list = []


def main():
    my_set = CustomSet()
    my_set.add("item 1")
    my_set.add("item 2")
    my_set.add("item 1")

    print(my_set.as_list())

    my_set.remove("item 2")
    print(my_set.as_list())

    try:
        my_set.remove("item 2")
    except KeyError:
        print("Item not removed, moving forward")

    my_set.clear()
    print(my_set.as_list())


if __name__ == "__main__":
    main()
