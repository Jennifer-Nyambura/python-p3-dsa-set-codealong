class MySet:
    def __init__(self, enumerable=[]):
        """
        Initialize the set. Accepts an optional iterable (like a list),
        and stores only unique values.
        """
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        """
        Check if the value exists in the set.
        O(1) runtime.
        """
        return value in self.dictionary

    def add(self, value):
        """
        Add a value to the set.
        O(1) runtime.
        """
        self.dictionary[value] = True
        return self

    def delete(self, value):
        """
        Remove a value from the set.
        O(1) runtime.
        """
        self.dictionary.pop(value, None)
        return self

    def size(self):
        """
        Return the number of elements in the set.
        O(1) runtime.
        """
        return len(self.dictionary)

    def clear(self):
        """
        Remove all values from the set.
        """
        self.dictionary.clear()
        return self

    def __str__(self):
        """
        Print the set in a human-readable format.
        Example: MySet: {1, 2, 3}
        """
        set_list = [str(key) for key in self.dictionary]
        return f"MySet: {{{', '.join(set_list)}}}"

    # ----- Bonus Methods -----
    def union(self, other_set):
        """
        Return a new set that is the union of this set and another.
        """
        new_set = MySet()
        for key in self.dictionary:
            new_set.add(key)
        for key in other_set.dictionary:
            new_set.add(key)
        return new_set

    def intersection(self, other_set):
        """
        Return a new set that is the intersection of this set and another.
        """
        new_set = MySet()
        for key in self.dictionary:
            if key in other_set.dictionary:
                new_set.add(key)
        return new_set

    def difference(self, other_set):
        """
        Return a new set with elements in this set but not in the other.
        """
        new_set = MySet()
        for key in self.dictionary:
            if key not in other_set.dictionary:
                new_set.add(key)
        return new_set

