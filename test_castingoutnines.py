from castingoutnines import CastingOutNines
from random import randint
from unittest import TestCase


class CastOutNinesTests(TestCase):
    def test_numbers(self, nbr_1: int = 17, nbr_2: int = 35):
        for operator in ["*", "+"]:
            con: CastingOutNines = CastingOutNines(
                nbr_1=nbr_1, nbr_2=nbr_2, operator=operator
            )
            self.assertTrue(expr=con.sanity_test)

    def test_10_random_numbers(self):
        for _ in range(10):
            self.test_numbers(nbr_1=randint(a=1, b=1000), nbr_2=(randint(a=1, b=1000)))
