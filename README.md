# Atividade de Comunicação entre Processos utilizando RPC

## Sobre o projeto

Este projeto foi desenvolvido como atividade acadêmica com o objetivo de demonstrar a comunicação entre processos utilizando **RPC (Remote Procedure Call)** em Python.

A aplicação permite que um programa cliente solicite a execução de operações matemáticas disponibilizadas por um servidor, recebendo os resultados por meio de chamadas remotas de procedimento.

## Objetivos

* Compreender o funcionamento da comunicação RPC.
* Implementar um servidor que disponibiliza funções remotamente.
* Desenvolver um cliente que realiza chamadas ao servidor.
* Demonstrar a troca de solicitações e respostas entre processos.

## Tecnologias utilizadas

| Tecnologia           | Descrição                     |
| -------------------- | ----------------------------- |
| Python 3             | Linguagem de programação      |
| XML-RPC              | Protocolo de chamadas remotas |
| `SimpleXMLRPCServer` | Implementação do servidor RPC |
| `xmlrpc.client`      | Cliente para comunicação RPC  |

## Estrutura do projeto

```text
atividade-rpc-python/
├── servidor.py
├── cliente.py
└── README.md
```

## Funcionalidades

O servidor disponibiliza as seguintes operações:

* **Soma:** adiciona dois números.
* **Subtração:** calcula a diferença entre dois números.
* **Multiplicação:** multiplica dois números.
* **Divisão:** divide dois números, tratando a divisão por zero.

## Como executar

### 1. Pré-requisitos

* Python 3 instalado.
* Terminal ou editor de código, como o Visual Studio Code.

Não é necessária a instalação de bibliotecas externas.

### 2. Iniciar o servidor

Abra o terminal na pasta do projeto e execute:

```bash
python servidor.py
```

O servidor ficará aguardando as solicitações dos clientes na porta 8000.

### 3. Executar o cliente

Abra um segundo terminal na mesma pasta e execute:

```bash
python cliente.py
```

O cliente realizará as chamadas remotas e exibirá os resultados.

## Exemplo de execução

Considerando os valores 10 e 5, o resultado esperado é:

```text
=== Calculadora RPC ===
Números utilizados: 10 e 5
Soma: 15
Subtração: 5
Multiplicação: 50
Divisão: 2.0
```

## Funcionamento da comunicação

1. O servidor inicia e registra as funções matemáticas.
2. O cliente estabelece uma conexão com o servidor.
3. O cliente envia os valores e solicita a execução de uma função.
4. O servidor executa o cálculo solicitado.
5. O resultado é retornado ao cliente.

## Conceitos aplicados

**RPC (Remote Procedure Call):** mecanismo que permite a um programa solicitar a execução de uma função em outro processo, como se fosse uma chamada local.

**Cliente:** programa responsável por enviar as solicitações.

**Servidor:** programa responsável por receber as solicitações, executar as operações e retornar os resultados.

**XML-RPC:** mecanismo que utiliza XML para representar os dados trocados durante as chamadas remotas.


