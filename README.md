# Jogo da Forca 🎮

<img align="center" alt="Ka-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"> <img align="center" alt="Ka-pycharm" height="30" width="120" src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white">

#
O código apresentado é um jogo da forca implementado em Python. Ele funciona da seguinte maneira:

1. Uma lista de palavras possíveis e suas respectivas dicas é criada.
2. Uma palavra é escolhida aleatoriamente da lista de palavras.
3. A palavra escolhida é armazenada como a palavra secreta e sua dica é exibida.
4. Uma lista de letras descobertas é criada, com "_" representando cada letra não descoberta da palavra secreta.
5. O jogador tem um número máximo de tentativas para adivinhar a palavra.
6. O jogo é iniciado e entra em um loop principal que continua até que o jogador vença ou perca.
7. Em cada iteração do loop, o estado atual do jogo é exibido, incluindo as letras descobertas, as letras erradas já tentadas e as tentativas restantes.
8. O jogador fornece uma letra como palpite.
9. A letra é validada, verificando se é uma única letra e se ainda não foi tentada anteriormente.
10. Se a letra estiver presente na palavra secreta, as ocorrências da letra são reveladas na lista de letras descobertas.
11. Se a letra não estiver presente na palavra secreta, ela é adicionada à lista de letras erradas e o número de tentativas é reduzido.
12. O jogo verifica se o jogador venceu, ou seja, se todas as letras da palavra secreta foram descobertas.
13. O jogo verifica se o jogador perdeu, ou seja, se esgotou o número de tentativas.
14. O jogo exibe uma mensagem de vitória ou derrota, juntamente com a palavra secreta, e encerra.

O código utiliza o módulo `random` para escolher uma palavra aleatória da lista de palavras possíveis. Além disso, faz uso de estruturas de dados como listas e dicionários para armazenar informações sobre as palavras e o estado do jogo. Também utiliza comandos de controle de fluxo, como loops e condicionais, para controlar o andamento do jogo.

Em resumo, o código implementa o jogo da forca, onde o jogador tenta adivinhar uma palavra secreta fornecendo letras como palpites. O jogo exibe informações sobre o estado do jogo, como letras descobertas, letras erradas e tentativas restantes, e verifica se o jogador venceu ou perdeu.
