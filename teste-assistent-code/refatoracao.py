from typing import List, Tuple

def calcular_estatisticas(numeros: List[float]) -> Tuple[float, float, float, float]:
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numeros (List[float]): Lista de números para calcular as estatísticas.

    Returns:
        Tuple[float, float, float, float]: Tupla contendo (total, média, máximo, mínimo).

    Raises:
        ValueError: Se a lista estiver vazia.
        TypeError: Se a entrada não for uma lista ou contiver elementos não numéricos.
    """
    if not isinstance(numeros, list):
        raise TypeError("A entrada deve ser uma lista de números.")

    if not numeros:
        raise ValueError("A lista não pode estar vazia.")

    # Verifica se todos os elementos são números
    if not all(isinstance(num, (int, float)) for num in numeros):
        raise TypeError("Todos os elementos da lista devem ser números.")

    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)

    return total, media, maximo, minimo

# Exemplo de uso
if __name__ == "__main__":
    lista_exemplo = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

    try:
        total, media, maximo, minimo = calcular_estatisticas(lista_exemplo)
        print(f"Total: {total}")
        print(f"Média: {media:.2f}")
        print(f"Maior: {maximo}")
        print(f"Menor: {minimo}")
    except (ValueError, TypeError) as e:
        print(f"Erro: {e}")