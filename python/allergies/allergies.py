from collections import OrderedDict


ALLERGIES = OrderedDict([
    ('cats', 128),
    ('pollen', 64),
    ('chocolate', 32),
    ('tomatoes', 16),
    ('strawberries', 8),
    ('shellfish', 4),
    ('peanuts', 2),
    ('eggs', 1),
])


class Allergies(object):
    """docstring for Allergies"""
    def __init__(self, score):
        self.score = self._generate_score(score)
        self._lst = []

    @property
    def lst(self):
        score = self.score
        for allergen, i in ALLERGIES.items():
            if i <= score:
                score -= i
                self._lst.append(allergen)
        return self._lst

    def is_allergic_to(self, allergen):
        return ALLERGIES[allergen] <= self.score

    def _generate_score(self, given_score):
        return given_score if given_score < 256 else given_score - 256
