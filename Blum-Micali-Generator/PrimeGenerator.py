from enum import Enum
from random import random, randrange


class PrimeTest(Enum):
    TRIAL_DIVISION = 0
    MILLER_RABIN = 1


class PrimeGenerator:
    def __init__(self):
        pass

    def __del__(self):
        pass

    @staticmethod
    def is_prime(number: int, algorithm: PrimeTest = PrimeTest.MILLER_RABIN) -> bool:
       
        if algorithm == PrimeTest.MILLER_RABIN:
            return PrimeGenerator._miller_rabin(number)
        elif algorithm == PrimeTest.TRIAL_DIVISION:
            return PrimeGenerator._trial_division(number)

    @staticmethod
    def _trial_division(number: int):
        i: int = 2
        while i < number:
            if number % i == 0:
                return False
            i += 1
        return True

    @staticmethod
    def _miller_rabin(number: int, iterations: int = 10):
      

        if number == 2 or number == 3:
            return True
        if not number & 1:
            return False

        def _check(a, s, d, n):
            x = pow(a, d, n)
            if x == 1:
                return True
            for i in range(s - 1):
                if x == n - 1:
                    return True
                x = pow(x, 2, n)
            return x == n - 1

        s = 0
        d = number - 1

        while d % 2 == 0:
            d >>= 1
            s += 1

        for i in range(iterations):
            a = randrange(2, number - 1)
            if not _check(a, s, d, number):
                return False
        return True

    @staticmethod
    def get_prime(digits: int = 10) -> int:
        
        number: int = round(random() * (10 ** digits))
        while not PrimeGenerator.is_prime(number):
            number += 1
        return number
