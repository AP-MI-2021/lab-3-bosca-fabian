from math import ceil, modf
from decimal import Decimal

def only_alternating_signs(lista_posibila_semn_alt):
    """
    Functia verifica daca lista are doar termeni la care le alterneaza semnul
    :param lista_posibila_semn_alt: list[int]
    :return: True daca se indeplineste conditia, False in caz contrar
    """
    for i in range(1, len(lista_posibila_semn_alt)):
        if lista_posibila_semn_alt[i] >= 0 and lista_posibila_semn_alt[i - 1] >= 0:
            return False
        if lista_posibila_semn_alt[i] * lista_posibila_semn_alt[i-1] > 0:
            return False
    return True


def digits_are_prime(numar):
    """
    Functia verifica daca cifrele unui numar sunt toate prime
    :param numar: int
    :return: True daca este indeplinita conditia, respectiv False daca nu
    """
    if numar == 0:
        return False
    if numar < 0:
        numar *= -1
    while numar:
        cifra = numar % 10
        if cifra != 2 and cifra != 3 and cifra != 5 and cifra != 7:
            return False
        numar = numar // 10
    return True


def only_prime_digits(lista_posibila_nr_cif_prime):
    """
    Functia verifica daca toate numerele din lista au toate cifrele prime
    :param lista_posibila_nr_cif_prime: list[int]
    :return: True daca se indeplineste conditia, False in caz contrar
    """
    for element in lista_posibila_nr_cif_prime:
        if not digits_are_prime(element):
            return False
    return True


def get_longest_alternating_signs(lista: list[int]) -> list[int]:
    """
    Functia obtine din o lista cea mai lunga sublista ale carei numere le alterneaza semnul
    In caz ca exista mai multe subliste care indeplinesc conditia se returneaza prima
    :param lista: list[int]
    :return lista_numere_semne_alternante: list[int] ~ cea mai lunga sublista care indeplineste conditia
    """
    lista_numere_semne_alternante = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista) + 1):
            if only_alternating_signs(lista[start:end]):
                if len(lista[start:end]) > len(lista_numere_semne_alternante):
                    lista_numere_semne_alternante = lista[start:end].copy()
    return lista_numere_semne_alternante


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([2, -4, 0, -1]) == [2, -4, 0, -1]
    assert get_longest_alternating_signs([13, -1, -2, 2]) == [13, -1]
    assert get_longest_alternating_signs([0, 0, -1, 10, -18]) == [0, -1, 10, -18]
    assert get_longest_alternating_signs([1, 2, 4, 6, 8]) == [1]
    assert get_longest_alternating_signs([-18, -29, -39, -33]) == [-18]


def get_longest_prime_digits(lista: list[int]) -> list[int]:
    """
    Functia obtine din o lista cea mai lunga sublista ale carei numere sunt formate doar din cifre prime
    In caz ca exista mai multe subliste care indeplinesc conditia se returneaza prima
    :param lista: list[int]
    :return lista_numere_cifre_prime: list[int] ~ cea mai lunga sublista care indeplineste conditia
    """
    lista_numere_cifre_prime = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista) + 1):
            if only_prime_digits(lista[start:end]):
                if len(lista[start:end]) > len(lista_numere_cifre_prime):
                    lista_numere_cifre_prime = lista[start:end].copy()
    return lista_numere_cifre_prime


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([4, 6, 8, 99]) == []
    assert get_longest_prime_digits([2, 3, 4, 5]) == [2, 3]
    assert get_longest_prime_digits([-123, -222, 0, 277, -332]) == [277, -332]
    assert get_longest_prime_digits([2]) == [2]


def citire_lista_intregi():
    lista = []
    dimensiune = int(input("Introduceti dimensiunea listei: "))
    while dimensiune:
        element = int(input("Introduceti elementul listei: "))
        lista.append(element)
        dimensiune -= 1
    return lista


def numar_cifre(numar):
    """
    Obtine numarul de cifre ale unui numar
    :param numar: int
    :return: int ~ numarul de cifre
    """
    nr_cifre = 0
    while numar:
        nr_cifre += 1
        numar //= 10
    return nr_cifre


def parte_fractionala(numar):
    """
    Obtine partea fractionala si o transforma intr-un numar intreg cu acelasi numar de cifre ca si partea intreaga
    :param numar: float
    :return: int ~ partea fractionala ca numar intreg
    """
    if numar < 0:
        numar *= -1
    nr_cifre = numar_cifre(int(numar))
    fractional = numar - int(numar)
    fractional = Decimal(fractional)
    fractional = round(fractional, nr_cifre)
    fractional = int(fractional * 10 ** nr_cifre)
    return fractional


def only_fractional_integer_part(lista_posibila_int_equals_fract):
    for element in lista_posibila_int_equals_fract:
        if abs(int(element)) != parte_fractionala(element):
            return False
    return True


def get_longest_equal_int_real(lista: list[float]) -> list[float]:
    """
    Functia obtine cea mai lunga subsecventa care are partea intreaga egala cu partea fractionala
    :param lista: list[float]
    :return: list[float] ~ cea mai lunga subsecventa care respecta conditia
    """
    lista_numere_int_float = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista) + 1):
            if only_fractional_integer_part(lista[start:end]):
                if len(lista[start:end]) > len(lista_numere_int_float):
                    lista_numere_int_float = lista[start:end].copy()
    return lista_numere_int_float


def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([12.45, 13.341 ,12.12, 13.13]) == [12.12, 13.13]
    assert get_longest_equal_int_real([-234.234, 21.21, 21.213]) == [-234.234, 21.21]
    assert get_longest_equal_int_real([1.1, 1.11, 1.111]) == [1.1]
    assert get_longest_equal_int_real([21.12, 433.433, -12.12, -13.13, 1.45]) == [433.433, -12.12, -13.13]


def citire_lista_reale():
    lista = []
    dimensiune = int(input("Introduceti dimensiunea listei: "))
    while dimensiune:
        element = float(input("Introduceti elementul listei: "))
        lista.append(element)
        dimensiune -= 1
    return lista


def main():
    lista = []
    while True:
        print("""
1. Citire date
        1.1 Numere intregi
        1.2 Numere reale
2. Determinare cea mai lunga subsecventa cu proprietatea 1(integers only)
3. Determinare cea mai lunga subsecventa cu prorpietatea 2(integers only)
4. Determinare cea mai lunga subsecventa cu proprietatea 3(float)
5. Iesire""")
        command = input("Introduceti comanda: ")
        if command == '5':
            break
        elif command == '1.1':
                lista = citire_lista_intregi()
        elif command == "1.2":
                lista = citire_lista_reale()
        elif command == '2':
            if len(lista) < 2:
                print("Lista nu este indeajuns de mare")
            else:
                lista_semne_alternante = get_longest_alternating_signs(lista)
                if len(lista_semne_alternante) == 1:
                    print("Semnele NU alterneaza")
                else:
                    print(lista_semne_alternante)
        elif command == '3':
            lista_nr_cifre_prime = get_longest_prime_digits(lista)
            if not lista_nr_cifre_prime:
                print("NU exista numere ale caror cifre sa fie doar prime")
            else:
                print(lista_nr_cifre_prime)
        elif command == '4':
            lista_nr_int_equals_fract = get_longest_equal_int_real(lista)
            print(lista_nr_int_equals_fract)
        elif command == '5':
            break
        else:
            print("Comanda invalida!!!")


test_get_longest_alternating_signs()
test_get_longest_prime_digits()
test_get_longest_equal_int_real()
main()