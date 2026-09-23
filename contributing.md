# Contribuindo com o projeto Cadastro de Pessoas

## Convenções de código

O projeto utiliza Python e segue as convenções de nomenclatura definidas no arquivo `.pylintrc`.

* Funções e métodos devem utilizar `snake_case`.
* Variáveis devem utilizar `snake_case`.
* Classes devem utilizar `PascalCase`.
* Argumentos de funções devem utilizar `snake_case`.
* Constantes devem utilizar `UPPER_CASE`.
* A indentação deve utilizar 4 espaços.
* As linhas devem possuir, preferencialmente, no máximo 100 caracteres.
* O código deve priorizar legibilidade e simplicidade.

## PyLint

O projeto utiliza o **PyLint** para análise estática do código.

Antes de realizar um commit, execute:

```bash
python -m pylint --rcfile=.pylintrc Cadastro.py
```

O projeto utiliza o arquivo `.pylintrc` para definir as regras da análise.

A pontuação esperada é **10.00/10.00**. Os apontamentos apresentados pelo PyLint devem ser analisados antes do commit. Correções devem ser realizadas quando contribuírem para a qualidade, legibilidade ou manutenção do código.

Não devem ser feitas alterações no código apenas para aumentar a pontuação do PyLint sem analisar o significado do apontamento.

## Commits

Os commits devem ser pequenos, objetivos e descrever claramente a alteração realizada.

Utiliza-se o padrão:

```text
tipo: descrição da alteração
```

Os principais tipos utilizados no projeto são:

* `feat`: adição de uma nova funcionalidade.
* `fix`: correção de um problema.
* `refactor`: alteração na estrutura interna do código sem mudança de comportamento.
* `chore`: alterações de configuração, organização ou manutenção do projeto.

Exemplos:

```text
feat: adiciona consulta de pessoa
fix: corrige validação da idade
refactor: divide função de análise de pessoa
chore: adiciona padrões de contribuição e configuração do pylint
```

As mensagens de commit devem ser objetivas e descrever a alteração realizada.

## Fluxo de contribuição

Antes de realizar um commit:

1. Verifique as alterações realizadas.
2. Execute o PyLint utilizando o `.pylintrc`.
3. Analise e corrija os apontamentos relevantes.
4. Faça um commit descrevendo claramente a alteração.
5. Evite misturar alterações não relacionadas no mesmo commit.
