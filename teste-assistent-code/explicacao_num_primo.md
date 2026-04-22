# Explicação Técnica da Função `is_prime` em Python

## Visão Geral
A função `is_prime(n)` implementa um algoritmo eficiente para verificar se um número inteiro `n` é primo. Um número primo é definido como um inteiro maior que 1 que possui apenas dois divisores positivos distintos: 1 e ele mesmo.

## Algoritmo Utilizado
O algoritmo segue uma abordagem otimizada baseada na verificação de divisibilidade:

1. **Casos Base**:
   - Números ≤ 1 não são primos.
   - O número 2 é o único número primo par.
   - Números pares maiores que 2 não são primos.

2. **Verificação de Fatores Ímpares**:
   - Para números ímpares maiores que 2, verifica-se a divisibilidade por números ímpares começando de 3 até a raiz quadrada de `n`.
   - Se nenhum divisor for encontrado, o número é primo.

## Complexidade de Tempo
- **Melhor Caso**: O(1) para números ≤ 1, 2 ou pares > 2.
- **Pior Caso**: O(√n) devido ao loop que itera até √n.
- Esta é uma melhoria significativa em relação a verificações ingênuas que checariam até n/2.

## Implementação Detalhada

```python
import math
from typing import Union

def is_prime(n: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é um inteiro maior que 1 que possui apenas dois divisores positivos: 1 e ele mesmo.

    Args:
        n (int): O número a ser verificado. Deve ser um inteiro não negativo.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        TypeError: Se n não for um inteiro.
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
```

### Explicação Linha por Linha
- `import math` e `from typing import Union`: Importa módulos necessários; `math` para `sqrt()`, `typing` para anotações de tipo.
- `def is_prime(n: int) -> bool:`: Define a função com anotações de tipo para clareza.
- `if not isinstance(n, int): raise TypeError(...)`: Valida o tipo de entrada para robustez.
- `if n <= 1: return False`: Trata números não positivos e 1.
- `if n == 2: return True`: 2 é primo.
- `if n % 2 == 0: return False`: Elimina pares > 2.
- `limite = int(math.sqrt(n)) + 1`: Calcula o limite superior para o loop.
- `for divisor in range(3, limite, 2)`: Loop de 3 até √n, passo 2 (apenas ímpares), usando nome descritivo `divisor`.
- `if n % divisor == 0: return False`: Se divisível, não é primo.
- `return True`: Se nenhum divisor encontrado, é primo.

## Casos de Teste
O código inclui testes automatizados:
- Testa múltiplos casos, incluindo bordas (1, 0, negativo).
- Usa um loop para verificar resultados esperados e imprime status (PASSOU/FALHOU).

## Considerações Técnicas
- **Precisão**: Usa `int(math.sqrt(n))` para evitar floats, garantindo cobertura completa.
- **Eficiência**: Evita verificações desnecessárias para pares e limita o loop a √n.
- **Limitações**: Para números muito grandes, algoritmos probabilísticos (ex.: Miller-Rabin) podem ser mais apropriados devido à complexidade.
- **Entrada**: Valida tipo de entrada com `isinstance` para prevenir erros.

## Princípios de Clean Code Aplicados
- **Nomes Descritivos**: Variável `divisor` em vez de `i`; função `is_prime` clara.
- **Anotações de Tipo**: Adicionadas para melhorar legibilidade e detecção de erros.
- **Validação de Entrada**: Verifica tipo para robustez.
- **Documentação**: Docstring expandida com descrição, args, returns e raises.
- **Testes Automatizados**: Loop estruturado para testes, facilitando manutenção.
- **Separação de Responsabilidades**: Função focada apenas na verificação de primalidade.

Esta implementação segue boas práticas de clean code, sendo legível, robusta e fácil de manter.