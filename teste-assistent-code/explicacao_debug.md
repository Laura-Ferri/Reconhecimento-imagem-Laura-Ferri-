# Explicação dos Erros no Código debug.py

## Erros Identificados

1. **Erro de Sintaxe na Linha 5**: A string no `input` está sem aspas. Deve ser `input("Preço do item 1? ")`.

2. **Erro de Tipo na Linha 15**: `desconto_cupom` é capturado como string, mas usado em operações matemáticas. Precisa ser convertido para float.

3. **Erro de F-string na Linha 23**: O print para Item 2 está sem o prefixo `f`, tornando-o uma string literal em vez de f-string.

4. **Erro de Comparação na Linha 27**: `desconto_cupom` é string, não pode ser comparado com 0. Após conversão, comparar com 0.0.

5. **Erro de Formatação na Linha 28**: `desconto_cupom` é string, não pode ser formatado como número. Após conversão, usar corretamente.

## Correções Aplicadas

- Adicionadas aspas na linha 5.
- Convertido `desconto_cupom` para float na linha 15.
- Adicionado `f` no print da linha 23.
- Ajustada a condição if para comparar com 0.0.
- Corrigida a formatação no print do desconto.