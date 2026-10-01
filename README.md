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
