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


def citire_lista():
    lista = []
    dimensiune = int(input("Introduceti dimensiunea listei: "))
    while dimensiune:
        element = int(input("Introduceti elementul listei: "))
        lista.append(element)
        dimensiune -= 1
    return lista


def main():
    lista = []
    while True:
        print("""
1. Citire date
2. Determinare cea mai lunga subsecventa cu proprietatea 1
3. Determinare cea mai lunga subsecventa cu prorpietatea 2
4. Iesire""")
        command = input("Introduceti comanda: ")
        if command == '4':
            break
        elif command == '1':
            lista = citire_lista()
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
        else:
            print("Comanda invalida!!!")


test_get_longest_alternating_signs()
test_get_longest_prime_digits()
main()
