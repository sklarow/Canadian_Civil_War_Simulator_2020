from random import choice


class Territory:
    def __init__(self, name: str):
        self.name = name
        self.border_territory = []
        self.curr_emp = None
        self.origin_emp = None

    def __str__(self):
        return self.name


class Empire:
    def __init__(self, homeland: Territory):
        self._conquered = [homeland]
        self._homeland = homeland
        homeland.curr_emp, homeland.origin_emp = (self, self)

    def size(self):
        return len(self._conquered)

    def get_conquered(self):
        return self._conquered

    def defeated(self):
        return self.size() == 0

    def gain_independence(self):
        return self._takeover(self._homeland)

    def conquer(self):
        borders_terr = self._borders()
        return self._takeover(choice(borders_terr))

    def name(self):
        return self._homeland.name

    def __str__(self):
        emp_str = self.name() + ":  "
        for terr in self.get_conquered():
            emp_str += terr.name + ", "
        return emp_str[:-2]

    def _borders(self):
        borders = []
        for conquered_terr in self.get_conquered():
            for terr in conquered_terr.border_territory:
                if not (terr in self.get_conquered()):
                    borders.append(terr)
        return borders

    def _takeover(self, terr: Territory):
        old_emp = terr.curr_emp
        old_emp.get_conquered().remove(terr)
        terr.curr_emp = self
        self.get_conquered().append(terr)
        return terr, old_emp
