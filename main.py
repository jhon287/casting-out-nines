from castingoutnines import CastingOutNines
from random import randint


def do_casting_out_nines(a: int, b: int, operator: str | None = None) -> None:
    if operator is not None:
        con: CastingOutNines = CastingOutNines(nbr_1=a, nbr_2=b, operator=operator)
    else:
        con: CastingOutNines = CastingOutNines(nbr_1=a, nbr_2=b)
    print(str(con) + f"\n{'-' * 20}")


def main() -> None:
    do_casting_out_nines(a=17, b=35)
    do_casting_out_nines(a=36994, b=99363, operator="+")
    for _ in range(10):
        nbr_1: int = randint(a=1, b=1000)
        nbr_2: int = randint(a=1, b=1000)

        for operator in ["*", "+"]:
            do_casting_out_nines(a=nbr_1, b=nbr_2, operator=operator)


if __name__ == "__main__":
    main()
