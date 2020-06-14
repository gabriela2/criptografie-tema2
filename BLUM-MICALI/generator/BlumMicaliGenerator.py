class BlumMicaliGenerator:
    a: int
    p: int
    root: int
    x_prev: int

    def __init__(self, base: int, modulus: int, root: int):
        self.a = base
        self.p = modulus
        self.root = root
        self.x_prev = self.root
        pass

    def __del__(self):
        pass

    @staticmethod
    def _modular_pow(base, exponent, modulus):
        result: int = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent >>= 1
            base = (base ** 2) % modulus
        return result

    def _generate_random_bit(self):
        x_i: int = BlumMicaliGenerator._modular_pow(self.a, self.x_prev, self.p)
        self.x_prev = x_i
        if x_i < (self.p - 1) / 2:
            return "1"
        else:
            return "0"

    def generate_random_number(self, bit_length: int) -> str:
        bin_number: str = ""
        j: int = 0
        while j < bit_length:
            bin_number += self._generate_random_bit()
            j += 1
        return bin_number
