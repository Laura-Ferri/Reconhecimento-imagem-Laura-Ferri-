import math
from typing import Union

def is_prime(n: int) -> bool:
    """Verifica se um número inteiro é primo.

    Um número primo é um inteiro maior que 1 que possui apenas dois divisores positivos: 1 e ele mesmo.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        TypeError: Se ``n`` não for um inteiro.
    """
    if not isinstance(n, int):
        raise TypeError("O argumento deve ser um inteiro.")

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Verifica divisibilidade por números ímpares até a raiz quadrada de n
    limite = int(math.sqrt(n)) + 1
    for divisor in range(3, limite, 2):
        if n % divisor == 0:
            return False

    return True

# Testes simples
if __name__ == "__main__":
    test_cases = [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (1, False),
        (0, False),
        (-5, False),
    ]

    for numero, esperado in test_cases:
        resultado = is_prime(numero)
        status = "PASSOU" if resultado == esperado else "FALHOU"
        print(f"is_prime({numero}) = {resultado} ({status})")