Exercício Django Clima

Este exercício envolve a criação de um aplicativo web usando o framework Django para rastrear informações climáticas de cidades. Abaixo está um resumo do que foi realizado:

Tecnologias Utilizadas:
Django: Um framework web Python poderoso e flexível.
Docker: Para empacotar o aplicativo com todas as dependências e facilitar a execução em qualquer ambiente.
Estrutura do Projeto:
O projeto está organizado em várias partes:

weather/models.py: Define os modelos de dados para City (cidade) e DailyWeather (clima diário) utilizando o ORM do Django.

weather/views.py: Contém funções de visualização que processam as solicitações HTTP e retornam respostas, incluindo o método de indexação para a página inicial e detalhes da cidade.

weather/urls.py: Mapeia as URLs para as funções de visualização correspondentes.

weather/templates: Contém os templates HTML para renderizar as páginas.

