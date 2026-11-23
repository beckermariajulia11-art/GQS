A. Clareza e legibilidade
[ S ]A1 - Os nomes das variáveis deixam claro o seu significado?
[ S ]A2 - É possível compreender o que cada trecho faz sem executar o programa?
[ N ]A3 - Textos e valores literais aparecem repetidos ao longo do código?

B. Duplicação
[ N ]B1 -Existe código repetido em pontos diferentes do programa?
[  ]B2 - A mesma regra está implementada em mais de um lugar?
[ N ]B3 - A busca de uma pessoa aparece repetida?
[ N ]B4 - A impressão dos dados de uma pessoa aparece repetida?

C. Estrutura e complexidade
[ N ]C1 - Há blocos muito extensos ou difíceis de acompanhar?
[ S ]C2 - É possível identificar rapidamente onde começa e termina cada responsabilidade?
[ N ]C3 - Menu, leitura de dados, regras e exibição estão misturados no mesmo trecho?

D. Entrada e validação de dados
[  ]D1 - Entradas inválidas podem causar comportamento inesperado?
[ S ]D2 - Existe verificação de faixa ou de plausibilidade para a idade?
[  ]D3 - Campos obrigatórios podem ser gravados vazios?

E. Consistência dos dados
[  ]E1 - Os dados de uma mesma pessoa estão espalhados em variáveis que podem se desencontrar?
[ S ]E2 - Existe regra clara para identificar unicamente uma pessoa?
[ N ]E3 - Há política definida para nomes duplicados?

F. Manutenibilidade e evolução
[ S ]F1 - Acrescentar um novo atributo à pessoa exigiria alterar muitos pontos do código?
[ N ]F2 - Uma nova operação faria o bloco principal crescer significativamente?
[ S ]F3 - Alterar a interface com o usuário exigiria alterar a lógica do sistema?

G. Comportamento e possíveis defeitos
[  ]G1 - O comportamento para uma pessoa inexistente é adequado e informativo?
[  ]G2 - Operações equivalentes tratam os mesmos dados de maneira coerente entre si?