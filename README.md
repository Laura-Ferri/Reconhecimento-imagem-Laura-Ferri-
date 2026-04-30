# Reconhecimento de Imagem - Laura Ferri Pereira

Este repositório contém exemplos e explicações de código Python para exercícios de lógica, depuração e refatoração, organizados dentro da pasta `teste-assistent-code`.

## Estrutura do Projeto

- `README.md` - documentação do projeto.
- `index.html` - arquivo HTML presente na raiz do workspace.
- `teste-assistent-code/`
  - `debug.py` - exemplo de cálculo de nota fiscal com entrada de usuário e exibição formatada.
  - `num_primos.py` - função para verificar se um número é primo, com testes simples.
  - `refatoracao.py` - função para calcular estatísticas básicas (total, média, máximo, mínimo) de uma lista de números.
  - `explicacao_debug.md` - explicações sobre os erros identificados e correções aplicadas no `debug.py`.
  - `explicacao_num_primo.md` - explicação técnica detalhada do algoritmo de verificação de número primo.
  - `explicacao_refatoracao.md` - explicação da refatoração de código e das boas práticas aplicadas em `refatoracao.py`.

## Objetivo

O projeto demonstra conceitos importantes de programação Python, incluindo:

- validação de entrada e tratamento de erros
- formatação de saída e mensagens para o usuário
- organização de código com funções reutilizáveis
- documentação e explicação técnica de algoritmos
- boas práticas de clean code

## Descrição dos Scripts

### `teste-assistent-code/debug.py`

Script interativo que lê dados do usuário para três itens, calcula o subtotal, aplica imposto de 10% e aplica um desconto percentual informado pelo usuário. Em seguida, exibe todos os valores formatados em uma saída de texto.

### `teste-assistent-code/num_primos.py`

Define a função `is_prime(n: int) -> bool` para verificar se um número inteiro é primo. A função:

- valida o tipo de entrada
- trata casos especiais (`n <= 1`, `n == 2`)
- elimina números pares maiores que 2
- testa divisores ímpares até a raiz quadrada de `n`

O script também contém um bloco de testes básicos para verificar resultados esperados.

### `teste-assistent-code/refatoracao.py`

Define a função `calcular_estatisticas(numeros: List[float]) -> Tuple[float, float, float, float]` que retorna:

- soma total
- média
- valor máximo
- valor mínimo

A função valida que a entrada é uma lista não vazia e que todos os elementos são numéricos.

## Como Executar

Certifique-se de ter Python 3 instalado.

No terminal, execute:

```powershell
python teste-assistent-code/debug.py
python teste-assistent-code/num_primos.py
python teste-assistent-code/refatoracao.py
```

## Dependências

O projeto usa apenas a biblioteca padrão do Python. Não há dependências externas.

## Observações

- A pasta `teste-assistent-code` contém tanto os scripts quanto a documentação explicativa dos exercícios.
- A documentação em Markdown (`explicacao_*.md`) detalha os erros encontrados, as escolhas de implementação e as melhorias aplicadas.
