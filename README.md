# Ações Códigos para buscar boas ações de acordo com os parâmetros do Stormer. 
## o que qual o propósito do projeto? 
Pegar as informações que foram passadas pelo Stormer

 - lucro líquido subindo nos últimos 5 anos;
 - Patrimônio Líquido subindo no últimos 5 anos;
 - Passível Elegível:
	 - Idealmente dividas devem estar caindo;
	 - Mas eventualmente uma empresa se endivida para crescer;
	 - Nesse caso, se a divida subiu, mas o patrimônio liquido subiu igualmente, então, temos menos risco.
 - P/L < 10;
 - Índice P/L <8;
	 - empresas que tem muito potencial de lucro vão ter P/L muito alto;
	 - o P/L tem que estar abaixo de 10 se o ROE estiver abaixo da taxa de juros; 
 - ROE acima da taxa de juros;
 - Volume de negociação > R$500.000,00/dia;


## fluxo para pegar dados
- pegar todas as ações -> https://statusinvest.com.br/acao/companiesnavigation?page=1&size=1000
- entrar em uma ação -> https://statusinvest.com.br/acoes/lame4
- lucro líquido + volume negociação -> https://statusinvest.com.br/acoes/lame4
- Patrimônio Líquido -> https://statusinvest.com.br/acao/getbsactivepassivechart?companyName=lojas-americanas&type=2
- dividas -> https://statusinvest.com.br/acao/getbsactivepassivechart?companyName=lojas-americanas&type=2
- P/L + ROE -> https://statusinvest.com.br/acao/indicatorhistorical
  - passar o ticker = 'ticker da ação' e time = 5