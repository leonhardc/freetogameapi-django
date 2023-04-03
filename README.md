<h1 align='center'>
    FreeToGame API Consumer com Python e Django
</h1>
<p align="center">
    <img src="https://img.shields.io/badge/Por-Leonardo%20Rodrigues%20da%20Costa-blue"/>
    <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-green"/>
</p>

<h2 align='center'>Tecnologias Utilizadas</h2>

<br>
<div align='center'>
    <img src='https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white'/>
    <img src='https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white'/>
    <img src='https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white'/>
    <img src='https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white'/>
    <img src='https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E'/>
    <img src='https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white'/>
</div>
<br>

<h2 align='center'>Sobre</h2>

Depois de um tempo estudando programação decidi usar python como minha linguagem principal e o motivo principal dessa escolha foi principalmente por sua interdisciplinaridade. Com python podemos desenvolver desde aplicações desktop e mobile até aplicações Web completas, podemos criar projetos inteiros e dashboads para análise de dados e podemos também usar essa linguagem para projetos robustos de aprendizado de máquina e processamento digital de imagens. Enfim, acho que já entenderam onde quero chegar, eu gosto da liberdade de escolher uma area de estudos e não ter que voltar à estaca zero em uma linguagem de programação. Por mais que qualquer uma dessas aplicações que citei nas linhas acima possam ser implementadas em alguma outra linguagem, python tem outro ponto que me encantou muito, sua facilidade de aprendizado e por isso uso python como linguagem principal e pretendo continuar usando em projetos futuros. 

O Projeto que irei apresentar nessa breve descrição tem um peso simbólico um pouco maior para mim do que outros projetos meus que também foram implementados em python ou em django, porque nele eu pensei, estruturei e configurei do zero, ou seja, meus erros e acertos nesse projeto vieram basicamente de mim. O que me deixa um pouco orgulhoso, visto que, por mais que não seja uma aplicação complexa, ela tem um pouco de mim e um pouco dos meus gostos.

Enfim, e do que se trata esse projeto? Esse projeto, implementado em python como linguagem principal e que usa o django como framework tem o intuito de ser uma página para consulta de detalhes sobre jogos dos mais variados tipos e plataformas. Os dados sobre cada jogos são reais e cedidos pela API do site [FreeToGame](https://www.freetogame.com) a [FreeToGame API](https://www.freetogame.com/api-doc). 

Esse projeto renderiza três templates, que serão mostrados logo a seguir.


<h2 align='center'>Página Inicial</h2>

Essa é a página inicial do projeto, onde a aplicação faz uma consulta diretamente a API e retorna o template [index.html](./consumer/templates/index.html).

<br>
<div>
    <img src="./img/img1.png"/>
</div>
<br>

Essa página conta com uma navbar que contem três elementos principais, contados da direita para esquerda:

* **Menu de Hamburger** que contém informações sobre o que o projeto faz.
* **Botão de games salvos** onde, ao clicá-lo, você será redirecionado para outra página que contém todos os games que você salvou para consultas posteriores. Obs.: Este botão só aparece no caso de você já ter salvo algum jogo, caso contrário ele fica oculto.
* **Logo da Aplicação** que também é um link para página principal da aplicação.

Logo abaixo da navbar você pode ver três filtros. Esses filtros foram construidos levandos em consideração os resultados que poderiam ser retornados da própria API, sendo assim, você pode filtrar os resultados:

* **Por plataforma** a API oferece três possibilidades nesse caso, todas as plataformas, jogos para PC ou jogos para browser.
* **Por categoria** do jogo. Ex.: fps, moba, mundo aberto ... 
* **Por ordem** retorna os resultados por uma ordem especificada no filtro, como por exemplo, por ordem de lançamento do jogo, ordem alfabética ...

Abaixo dos filtros estão os resultados da pesquisa ou todos os jogos carregados inicialmente. Cada jogo conta com dois botões, um botão de detalhes, onde ao clicá-lo você será redirecionado para página de detalhes do jogo e o botão salvar, para consultas posteriores.

A página de detalhes do jogo é mostrada jogo a seguir.

<h2 align='center'>Detalhes</h2>

Nesse template estão todos os detalhes de cada jogo fornecidos pela API, renderizados de uma maneira amigável. 

<br>
<div>
    <img src="./img/img2.png"/>
</div>
<br>

Essa página conta com três seções, onde a primeira mostra a thumnail do game e seus requisitos mínimos, caso esse game seja para PC. A segunda seção conta com uma descrição do jogo seguido de uma série de screenshots do game que serão renderizadas se a API fornecer essas informações e em seguida uma seção sobre informações comerciais do game, além de links externos para a página do game ou para a profile do game no site do FreeToGame. 

O terceiro e ultimo template é o mostrado a seguir, o template de games salvos.

<h2 align='center'>Games Salvos</h2>

Essa é a página mais simples contando somente com os cards referentes a cada game que você salvou no decorrer da sua pesquisa na página inicial. 

<br>
<div>
    <img src="./img/img3.png"/>
</div>
<br>

A única particularidade de cada card desse template em relação aos cards do template da página inicial é que cada um contém um botão para excluir o game da lista de games salvos.

<h2 align='center'>Referências</h2>

* [FreeToGame API](https://www.freetogame.com/api-doc)
* [Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Django Docs](https://docs.djangoproject.com/en/4.2/)


