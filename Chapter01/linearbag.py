class Bag:
    # construct an empty bag
    def __init__(self):
        self._theItems = list()
    # return the length of the bag
    def __len__(self):
        return len(self._theItems)
    # determine the existance of the item
    def __contains__(self, item):
        return item in self._theItems
    # add items to the bag
    def add(self, item):
        return self._theItems.append(item)
    # remove an iten from the list
    def remove(self, item):
        assert item in self._theItems
        ndx = self._theItems.index(item)
        return self._theItems.pop(ndx)
    def show(self):
        print('The items in the bag', self._theItems)

bag = Bag()
bag.add(32)
bag.add(45)
bag.add(25)
bag.remove(25)
print(bag.__len__())
bag.show()