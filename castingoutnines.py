from operator import add, mul


class CastingOutNines:
    def __init__(
        self, nbr_1: int, nbr_2: int, operator: str = "*", auto_do: bool = True
    ) -> None:
        allowed_operators: tuple[str, str] = ("+", "*")

        self._nbr_1 = nbr_1
        self._nbr_2 = nbr_2
        self._operator = operator

        if operator == "*":
            self._operator_function = mul
        elif operator == "+":
            self._operator_function = add
        else:
            raise ValueError(
                f"Unkown operation: '{operator}'. Allowed operations: {allowed_operators}"
            )

        if auto_do:
            self.do()

    def __str__(self) -> str:
        return "\n".join(
            [
                f"Number 1   : {self.nbr_1} ({self.__get_sum_2_one_digit(nbr=self.nbr_1)})",
                f"Number 2   : {self.nbr_2} ({self.__get_sum_2_one_digit(nbr=self.nbr_2)})",
                f"Operator   : {self.operator}",
                f"Result     : {self.result} ({self.__get_sum_2_one_digit(nbr=self.result)})",
                f"Sanity Test: {'OK' if self.__sanity_test() else 'NOK'}",
            ]
        )

    def __get_sum_2_one_digit(self, nbr: int) -> int:
        result: int = nbr

        while result > 10:
            result = sum([int(nbr_char) for nbr_char in str(result)])

        return result

    def do(self) -> None:
        self._result = self._operator_function(self.nbr_1, self.nbr_2)

        if not self.__sanity_test():
            raise ArithmeticError(f"{self.nbr_1=} {self.nbr_2=} {self.result=}")

    def __sanity_test(self) -> bool:
        return self.__get_sum_2_one_digit(
            nbr=self._operator_function(
                self.__get_sum_2_one_digit(nbr=self.nbr_1),
                self.__get_sum_2_one_digit(nbr=self.nbr_2),
            )
        ) == self.__get_sum_2_one_digit(nbr=self.result)

    @property
    def nbr_1(self) -> int:
        return self._nbr_1

    @property
    def nbr_2(self) -> int:
        return self._nbr_2

    @property
    def result(self) -> int:
        return self._result

    @property
    def sanity_test(self) -> bool:
        return self.__sanity_test()

    @property
    def operator(self) -> str:
        return self._operator
