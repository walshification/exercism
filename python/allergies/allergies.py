ALLERGIES = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}


class Allergies:
    """Representation of a person's allergies.

    Attributes:
        score (int): The allergy score provided by input.
    """

    def __init__(self, score: int) -> None:
        self.score = score
        self.lst = [
            allergen for allergen in ALLERGIES.keys() if self.allergic_to(allergen)
        ]

    def allergic_to(self, allergen: str) -> bool:
        """Returns True if a person is allergic to the allergen.

        :param allergen: str - something a person might be allergic to.
        :return bool: True if allergic; otherwise, False
        """
        return self.score & ALLERGIES[allergen] > 0
