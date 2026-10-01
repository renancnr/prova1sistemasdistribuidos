# Atividade Prática: Comunicação RPC em Python

## Problema da empresa

A empresa precisa disponibilizar um cálculo para que outro programa possa solicitá-lo. Para solucionar esse problema, foi utilizada a comunicação RPC (Remote Procedure Call), permitindo que um cliente solicite a execução de um cálculo a um servidor.

## Arquivos do projeto

| Arquivo | Descrição |
|---|---|
| `servidor.py` | Recebe a chamada RPC, executa o cálculo e retorna o resultado. |
| `cliente.py` | Solicita o cálculo ao servidor e exibe a resposta. |

## Tecnologias utilizadas

- Python 3
- XML-RPC
- Comunicação entre processos

## Como executar

1. Abra um terminal na pasta do projeto.
2. Inicie o servidor:

   ```bash
   python servidor.py
   ```

3. Abra outro terminal na mesma pasta.
4. Execute o cliente:

   ```bash
   python cliente.py
   ```

## Resultado esperado

```text
Solicitação enviada ao servidor RPC.
Cálculo solicitado: 10 + 5
Resultado recebido: 15
```

## Respostas da atividade

**Em qual programa foi executado o cálculo?**

No programa `servidor.py`.

**Qual programa iniciou a solicitação?**

O programa `cliente.py`.

**O que aconteceria com o cliente se o servidor estivesse desligado?**

O cliente não conseguiria receber o resultado e apresentaria um erro de conexão, pois o servidor não estaria disponível.

## Conclusão

A atividade demonstrou que a comunicação RPC permite que um cliente solicite a execução de um cálculo a um servidor e receba o resultado, facilitando a comunicação e o compartilhamento de funcionalidades entre programas.

## Autor

CNR

*Projeto desenvolvido para fins acadêmicos.*
