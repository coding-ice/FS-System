from collections import abc


class GooseSpam:
    def __iter__(self):
        pass


g = GooseSpam()
print(isinstance(g, abc.Iterable))
print(issubclass(GooseSpam, abc.Iterable))