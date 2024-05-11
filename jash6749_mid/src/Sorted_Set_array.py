"""
-------------------------------------------------------
Array version of the Sorted_Set ADT.
-------------------------------------------------------
Author: Jashanpreet Singh Jashanpreet Singh
ID:     169046749
Email:  jash6749@mylaurier.ca
__updated__ = "2024-02-28"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy


class Sorted_Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_Set.
        Use: source = Sorted_Set()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            Creates a new Sorted_Set object. (Sorted_Set)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            True if source is empty, False otherwise. (boolean)
        -------------------------------------------------------
        """
        # your code here
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            the number of values in source. (int)
        -------------------------------------------------------
        """
        # your code here
        count = 0
        for _ in range(len(self._values)):
            count += 1
        return count

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the occurrence of key in self.
        Private helper method.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            i - the index of the only occurrence of key in
                self, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        # your code here
        length = len(self._values)
        ind = None
        f_half = 0
        s_half = length - 1
        while f_half <= s_half:
            i = f_half + (s_half-f_half)//2
            if self._values[i] == key:
                ind = i
            elif self._values[i] < key:
                f_half = i + 1
            else:
                s_half = i - 1

        if ind is None:
            ind = -1
        return ind

    def add(self, value):
        """
        -------------------------------------------------------
        If value does not already exist in source, adds a copy of value
        to source. Returns True if value is added, False otherwise.
        Values in source must remain sorted.
        Use: added = source.add(value)
        -------------------------------------------------------
        Parameters:
            value - data (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            added - True if value added to source, False otherwise. (boolean)
        -------------------------------------------------------
        """
        added = True
        # Index of beginning of subarray to search.
        low = 0
        # Index of end of subarray to search.
        high = len(self._values) - 1

        while low <= high and added:
            # Find the middle of the current subarray.
            # (avoids overflow on large values vs (low + high)//2
            mid = (high - low) // 2 + low

            if self._values[mid] == value:
                # value already in set
                added = False
            elif self._values[mid] > value:
                # search the left subarray.
                high = mid - 1
            else:
                # Default: search the right subarray.
                low = mid + 1

        if added:
            self._values.insert(low, deepcopy(value))
        return added

    def _rem_set(self, key):
        i = self._binary_search(key)
        if i != -1:
            for v in range(i, len(self._values)-1):
                self._values[v] = self._values[v+1]
            self._values[:] = self._values[:-1]
            ret = True
        else:
            ret = False
        return ret

    def discard(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source that matches key.
        Returns None if key not in source.
        Use: value = source.discard(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            value - the full value matching key, None otherwise. (*)
        -------------------------------------------------------
        """
        # your code here
        i = self._binary_search(key)
        if i == -1:
            value = None
        else:
            value = self._values[i]
            self._rem_set(key)
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Returns True if source contains key, False otherwise.
        Use: contains = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        # your code here
        i = self._binary_search(key)
        if i == -1:
            ret = False
        else:
            ret = True
        return ret

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            value - a copy of the full value matching key, otherwise None (*)
        -------------------------------------------------------
        """
        # your code here
        i = self._binary_search(key)
        if i == -1:
            ret = None
        else:
            ret = deepcopy(self._values[i])
        return ret

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Determines whether source == target.
        If source and target are of the same length and contain the same values,
        returns True, otherwise returns False.
        Order is significant.
        Use: equals = source == target
        -------------------------------------------------------
        Parameters:
            target - another sorted set (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3} == {1,2,3}: True
            {1,2,3} == {1,2,4}: False
            {1,2,3} == {1,2,3,4}: False
        -------------------------------------------------------
        """
        # your code here
        eq = True
        if len(self._values) != len(target._values):
            eq = False
        else:
            for i in range(len(self._values)):
                if self._values[i] != target._values[i]:
                    eq = False

        return eq

    def issubset(self, target):
        """
        ---------------------------------------------------------
        Tests whether every value in source is also in target.
        Use: subset = source.issubset(target)
        -------------------------------------------------------
        Parameters:
            target - another Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            subset - True if all values in source are also in target,
                False otherwise. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3}.issubset({0,1,2,3,4}): True
            {1,2,3}.issubset({1,2,4,5}): False
        -------------------------------------------------------
        """
        # your code here
        sub = True
        for val in self._values:
            contains = val in target._values
            if not contains:
                sub = False
        return sub

    def issuperset(self, target):
        """
        ---------------------------------------------------------
        Test whether every value in target is also in source.
        Use: superset = source.issuperset(target)
        -------------------------------------------------------
        Parameters:
            target - another Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            superset - True if all values in target are also in source,
                False otherwise. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3}.issuperset({0,1,2,3,4}): False
            {1,2,3,4,5}.issuperset({1,2,4,5}): True
        -------------------------------------------------------
        """
        # your code here
        super = True
        for val in self._target:
            contains = val in self._values
            if not contains:
                super = False
        return super

    def isdisjoint(self, target):
        """
        -------------------------------------------------------
        Return True if source has no values in common with target.
        Sorted_Sets are disjoint if and only if their intersection
        is the empty Sorted_Set.
        Use: disjoint = source.isdisjoint(target)
        -------------------------------------------------------
        Parameters:
            target - a Sorted_Set to compare against source. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            disjoint - True if source has no values in common with target,
                False otherwise. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3}.isdisjoint({4,5,6,7}): True
            {1,2,3}.isdisjoint({1,4,5,6,7}): False
        -------------------------------------------------------
        """
        # your code here
        dis = True
        for value in self._values:
            if value in target._values:
                dis = False
        return dis

    def intersection(self, target):
        """
        -------------------------------------------------------
        Return a new Sorted_Set with copies of values common to source and target.
        Order must be preserved.
        Use: new_set = source.intersection(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based sorted set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            new_set - the intersection of source and target. (Sorted_Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.intersection({3,4,5}): {3}
            {1,2,3}.intersection({4,5,6}): {}
        -------------------------------------------------------
        """
        # your code here
        new = Sorted_Set()
        for value in self._values:
            if value in target._values and value not in new._values:
                new.add(value)

        return new

    def union(self, target):
        """
        -------------------------------------------------------
        Return a new Sorted_Set with copies of all unique values from source and target.
        Order must be preserved.
        Use: new_set = source.union(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based sorted set (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            new_set - the union of source and target (Sorted_Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.union({3,4,5}): {1,2,3,4,5}
            {1,2,3}.union({4,5,6}): {1,2,3,4,5,6}
        -------------------------------------------------------
        """
        # your code here
        new = Sorted_Set()
        for val in self._values:
            new.add(val)
        for val in target._values:
            new.add(val)
        return new

    def difference(self, target):
        """
        -------------------------------------------------------
        Return a new Sorted_Set with copies of values in source that are not in target.
        Order is preserved.
        Use: new_set = source.difference(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based sorted set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            new_set - the difference of source and target. (Sorted_Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.difference({3,4,5}): {1,2}
            {2,3,4}.difference({1,2,3,4,5}): {}
        -------------------------------------------------------
        """
        # your code here
        new = Sorted_Set()
        for val in self._values:
            contains = val in target._values
            if not contains:
                new.add(val)
        return new

    def symmetric_difference(self, target):
        """
        -------------------------------------------------------
        Return a new set with copies of values in either source or target but not both.
        Order must be preserved.
        Use: new_set = source.symmetric_difference(target)
        -------------------------------------------------------
        Parameters:
            target - an array-based Set. (Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            new_set - the symmetric difference of source and target. (Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.symmetric_difference({3,4,5}): {1,2,4,5}
            {1,2,3}.symmetric_difference({1,2,3,4,5}): {4,5}
        -------------------------------------------------------
        """
        # your code here
        new = Sorted_Set()
        for val in self._values:
            if val not in target._values:
                new.add(deepcopy(val))
        for val in target._values:
            if val not in self._values:
                new.add(deepcopy(val))
        return new

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a Sorted_Set
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
            value - the next value in the Sorted_Set. (*)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
