# calculator

![Pipeline](https://github.com/lucasmarques73/node-api-heroku/workflows/Pipeline/badge.svg) 

---

Projeto realizado para gerenciamento de calculos matemáticos

Foi criado uma Api Rest, utilizando os seguintes recursos:

- Linguagem: Python;

- Frameworks/Bibliotecas: Unittest e FastAPI;

- Arquetetura em camadas: Test, Src;

- Pipeline: Azure DevOps

- Cloud: Azure

Funcionalidades implementadas:

- Calculo da equação de 2 grau (Bhaskara)

---

## Linguagem

- ### Python

Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.

---

## Frameworks/Bibliotecas

- ### Unittest

O framework de testes unitários unittest foi originalmente inspirado no JUnit e tem um sabor semelhante contendo as principais estruturas de teste de unidades existentes em outras linguagens. Ele suporta a automação de testes, compartilhamento de configuração e código de desligamento para testes, agregação de testes em coleções e independência dos testes do framework de relatórios.

- ### Flask

Flask é um pequeno framework web escrito em Python. É classificado como um microframework porque não requer ferramentas ou bibliotecas particulares, mantendo um núcleo simples, porém, extensível.

---

## Arquetetura em camadas

- ### test

Responsável de realizar testes unitários a camada src.

- ### src

Em ciência da computação e teoria da informação , compressão de redundância de conjunto 'set redundancy compression' (SRC) são métodos de compressão de dados que exploram redundâncias entre conjuntos de dados individuais em um conjunto.

Foi adicionado as seguintes subCamadas: domain, api

- ### domain

Responsável por representar conceitos, informações e regras sobre a situação do negócio. Aqui, um estado que reflete a situação de negócio é controlado e usado, embora os detalhes técnicos de armazenagem sejam delegados à infraestrutura. Esta é o coração do software do negócio.

- ### api

Responsável por mostrar informações ao usuário e interpretar os comandos do usuário. O agente externo pode, as vezes, ser outro sistema de computador em vez de usuário.
       
 ---
 
# Como executar o projeto ?

## Rodando o projeto localmente

1 - Verifique se o computador possui python instalado e qual a versão executando o comando abaixo caso o mesmo esteja com uma versão diferente da 3.10x, será necessário realizar a atualização/instalação para que o projeto execute corretamente;

Comando para validar a versão do python:

- Windows:
~~~ bash
python --version
~~~

- Linux/Mac
~~~ bash
python3 --version
~~~

Link para passo-a-passo de como atualizar/instalar a linguagem no seu computador:

- Windows: https://www.python.org/downloads/windows/

- Mac: https://www.python.org/downloads/macos/

- Linux:
~~~ bash
sudo apt-get install python 3.10.2
~~~

---

2 - Realize o clone do projeto para o local que desejar em seu computador executando o seguinte comando:

~~~~bash
git clone https://github.com/ZoeStyle/calculator.git
~~~~

3 - Navegue ate a pasta api dentro do projeto e execute o seguinte comando:

Windows:
~~~~bash
python -u "DIRETORIO\calculation\src\api\main.py"
~~~~

Linux/Mac:
~~~~bash
python3 -u "DIRETORIO\calculation\src\api\main.py"
~~~~