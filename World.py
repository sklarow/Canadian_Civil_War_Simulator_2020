from Empterr import Territory, Empire
from random import randint, choice


class World:
    def __init__(self, region_data: list):
        self._empires = []
        self._territories = []
        for info in region_data:
            self._territories.append(Territory(info[0]))
            self._empires.append(Empire(self._territories[len(self._territories) - 1]))
        for i in range(len(region_data)):
            info = region_data[i][1]
            terr = self._territories[i]
            for name in info:
                terr.border_territory.append(self._find_territory(name))
        self._alive = len(self._empires)
        self._latest_action = "war begins"
        self._winner = None

    def _find_territory(self, terr_name):
        for terr in self._territories:
            if terr.name == terr_name:
                return terr
        raise Exception("Territory doesn't exist")

    def update(self):
        not_chosen = True
        while not_chosen:
            chosen_empire = choice(self._empires)
            if chosen_empire.defeated():
                if randint(0, 50) == 0:
                    old_emp = chosen_empire.gain_independence()[1]
                    self._latest_action = chosen_empire.name() + " gained independence from " + old_emp.name()
                    not_chosen = False
            else:
                conquered_territory, old_emp = chosen_empire.conquer()
                self._latest_action = chosen_empire.name()+" conquered "+conquered_territory.name
                self._latest_action += " from " + old_emp.name()
                if old_emp.defeated():
                    self._latest_action += '\n' + old_emp.name() + " is completely defeated"
                not_chosen = False
        self._alive = 0
        for emp in self._empires:
            if not emp.defeated():
                self._alive += 1
        if self.united():
            for emp in self._empires:
                if not emp.defeated():
                    self._winner = emp
                    break

    def not_united(self):
        return self._alive != 1

    def united(self):
        return self._alive == 1

    def winner(self):
        return self._winner

    def __str__(self):
        world_str = ""
        world_str += self._latest_action + "\n\n"
        for emp in self._empires:
            world_str += str(emp) + '\n'
        return world_str
