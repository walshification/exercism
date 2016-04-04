# -*- coding: utf-8 -*-
ALLERGIES = {
    'eggs': 1,
    'peanuts': 2,
    'shellfish': 4,
    'strawberries': 8,
    'tomatoes': 16,
    'chocolate': 32,
    'pollen': 64,
    'cats': 128,
}


class Allergies(object):
    """Object representation of a person's allergies.

    Attributes:
        score (int): The allergy score provided by input.
    """
    def __init__(self, score):
        self.score = score
        self._lst = []

    @property
    def lst(self):
        """list: All the allergies a person has."""
        if not self._lst:
            self._lst = [a for a in ALLERGIES.keys() if self.is_allergic_to(a)]
        return self._lst

    def is_allergic_to(self, allergen):
        """Determines if a person is allergic to a given allergen
        using a 'bitwise and' comparison of the allergen and allergy
        score.

        Args:
            allergen (str): something a person might be allergic to.

        Returns:
            bool: True if allergic; otherwise, False
        """
        return self.score & ALLERGIES[allergen] > 0
