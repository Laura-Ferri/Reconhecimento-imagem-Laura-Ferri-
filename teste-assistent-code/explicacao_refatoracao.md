# Explicação do Código em refatoracao.py

## Visão Geral
O arquivo `refatoracao.py` foi refatorado para calcular estatísticas básicas de uma lista de números (soma total, média, valor máximo e valor mínimo) seguindo princípios de clean code: legibilidade, nomenclatura descritiva, validação de entrada e uso de funções built-in do Python.

## Código Refatorado

```python
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
```

## Explicação Detalhada

### Função `calcular_estatisticas(numeros)`
- **Propósito**: Calcula soma, média, máximo e mínimo de uma lista de números de forma robusta.
- **Parâmetros**: `numeros` (List[float]) - lista de números.
- **Retorno**: Tupla (float, float, float, float) com (total, média, máximo, mínimo).
- **Validações**:
  - Verifica se a entrada é uma lista.
  - Garante que a lista não está vazia.
  - Confirma que todos os elementos são números (int ou float).

#### Passo a Passo
1. **Validação de Tipo e Conteúdo**:
   - Usa `isinstance` para verificar tipos.
   - `all()` com generator para checar se todos são numéricos.
   - Levanta exceções claras para erros.

2. **Cálculo das Estatísticas**:
   - `total = sum(numeros)`: Usa função built-in `sum()` para eficiência.
   - `media = total / len(numeros)`: Calcula média aritmética.
   - `maximo = max(numeros)` e `minimo = min(numeros)`: Usa built-ins `max()` e `min()`.

3. **Retorno**:
   - Retorna tupla com os valores calculados.

### Código Principal
- **Lista de Exemplo**:
  ```python
  lista_exemplo = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
  ```
  - Nome descritivo para a variável.

- **Chamada Segura**:
  ```python
  try:
      total, media, maximo, minimo = calcular_estatisticas(lista_exemplo)
  ```
  - Usa `try-except` para capturar e exibir erros.

- **Impressão Formatada**:
  ```python
  print(f"Total: {total}")
  print(f"Média: {media:.2f}")
  ```
  - F-strings para legibilidade; formatação para média com 2 casas decimais.

## Melhorias Aplicadas (Clean Code)
- **Nomenclatura Descritiva**: Função e variáveis com nomes claros (ex.: `calcular_estatisticas`, `total`, `media`).
- **Anotações de Tipo**: Adicionadas para clareza e detecção de erros.
- **Docstring Completa**: Documenta propósito, parâmetros, retorno e exceções.
- **Validação Robusta**: Previne erros comuns com verificações de entrada.
- **Uso de Built-ins**: `sum()`, `max()`, `min()` tornam o código conciso e eficiente.
- **Tratamento de Erros**: Exceções informativas em vez de falhas silenciosas.
- **Legibilidade**: Código estruturado, comentários explicativos, f-strings.
- **Eficiência**: Eliminação de loops manuais; operações em O(n) otimizadas.

## Código Original (para Comparação)
O código original tinha nomes abreviados, loops manuais, falta de validação e risco de erros. A refatoração transforma-o em um código profissional, fácil de entender e manter.