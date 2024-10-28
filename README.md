<div align='center'>
<img src="https://github.com/douglasaturnino/elasticidade-de-preco/assets/95532957/f5b73b07-406b-4835-b963-072764985703"  width=700px/>
</div>

Este é um projeto fictício. A empresa, o contexto e as perguntas de negócios não são reais. Este portfólio está seguindo as recomendações da Comunidade DS. 

# Descrição do Problema:

Uma empresa de varejo de eletrônicos está enfrentando uma diminuição nas vendas de um determinado produto ao longo dos últimos trimestres. A equipe de marketing suspeita que o aumento do preço pode estar afetando adversamente a demanda pelo produto. Eles precisam determinar a elasticidade preço da demanda para este produto específico, a fim de entender como as mudanças nos preços afetam as vendas e otimizar a estratégia de preços para maximizar a receita.

# Objetivos do Projeto:

Calcular a Elasticidade Preço da Demanda: Usar dados históricos de vendas e preços para calcular a elasticidade preço da demanda para o produto em questão. Isso ajudará a entender se o produto é elástico (ou seja, pequenas mudanças no preço resultam em grandes mudanças na demanda) ou inelástico (mudanças no preço têm pouco impacto na demanda).

Prever o Impacto de Mudanças de Preço: Com base na elasticidade preço da demanda calculada, prever como as mudanças planejadas nos preços afetarão as vendas. Isso permitirá à empresa tomar decisões informadas sobre ajustes de preço para maximizar a receita ou volume de vendas, dependendo dos objetivos estratégicos.

Recomendações Estratégicas: Com base nos resultados da análise de elasticidade preço da demanda, recomendar uma estratégia de precificação que equilibre a maximização da receita com a manutenção ou aumento da participação de mercado. Isso pode envolver ajustes de preços sazonais, promoções ou reestruturação de pacotes de produtos.

# Premissas de negócio

Todos os produtos de dados entregues devem ser acessíveis via internet.

O planejamento da solução será validado com os times de negócio, visando garantir que as soluções desenvolvidas sejam úteis na sua tomada de decisão.

Só serão feita a elasticidade de preço nos produtos com uma significancia estatistica maior que 5%. 

# Planejamento da solução

## Saida
- Um grafico com a elesticidade de preços e os nomes do produtos 
- Uma tabela com as elasticidade de preços e os nomes do produtos 

## Processo
Baixar os dados e ler os dados

Executar o processo de limpeza de dados como:

renomear colunas

renomear categorias
mudar de tipo de variável, caso necessário

Estatística descritiva com visualização

Feature Engineering

Machine Learning

Elasticidade

Business Performance

Cross Price Elasticity

## Entrada
Não teremos entrada de dados feita pelo usuario.

# Conclusão
O objetivo foi alcançado, dado que o produto de dados foram gerados com sucesso. O funcionario pode utilizar a ferramenta criado para fazer a elasticidade de preço.

O dashboard pode ser acessado por[aqui](https://elasticidade-de-preco-dso.streamlit.app/)

# Próximos passos

- O usuario pode escolher a quantia de desconto para casa produto
- Fazer a elasticidade cruzada para os produtos alternativos ou podem ser substituidos
- Pagar mais dados para fazer a elasticidade de preço para uma quantidade maior de produtos.