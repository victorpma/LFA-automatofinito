# LFA- Atividade de Implementação 1

## Problema
> O trabalho prático consiste na implementação de um programa que permita cadastrar e testar autômatos finitos. A solução deve permitir que o usuário cadastre seu próprio autômato finito determinístico ou não-determinístico, indicando os estados, as transições e valores do alfabeto. Após o cadastro deve ser possível testar se uma determinada palavra faz parte ou não da linguagem representada pelo autômato.

> Caso cadastre um não-determinístico, deve-se aplicar a transformação para o determinístico e fazer o teste da palavra usando o autômato determinístico (neste caso, apresente o autômato determinístico antes de testar a palavra). 

> A implementação do não-determinístico com transição vazia é opcional.  

## Como funciona a aplicação

Para cadastrar um autômato na aplicação será necessário formatar um JSON localizado na pasta raiz do projeto ```/InsiraSeuAutomatoAqui/automato.json```, esse arquivo contém os dados do Autômato, abaixo um exemplo:

```
{
  "alfabeto": ["a", "b"],
  "estadoInicial": "q0",
  "estadoFinal": ["q3", "q4"],
  "transicoes": {
    "q0": {
      "a": "q1",
      "b": "q2"
    },
    "q1": {
      "a": "q7",
      "b": "q3"
    },
    "q2": {
      "a": "q4",
      "b": "q6"
    },
    "q3": {
      "a": "q1",
      "b": "q7"
    },
    "q4": {
      "a": "q6",
      "b": "q2"
    }
  }
}
```

No JSON acima possui dados necessários para que a aplicação consiga ler os dados:

- alfabeto: Todos os símbolos que o autômato consegue ler;
- estadoInicial: Representa o estado inicial do autômato;
- estadoFinal: Representa o estado final do autômato;
- transicoes: Para cada transição de estado será necessário informar um objeto contendo o nome do estado e dentro do objeto será informado como atributos os estado que cada símbolo poderá ir, ou seja as transições daquele determinado estado.

O exemplo acima consiste em um autômato finito não-determinístico que reconhece a linguagem do alfabeto {a, b} onde palavras contenham a's e b's sempre de forma alternada: Ou seja palavras do tipo: ababab, ababa, bababa, babab e assim por diante. Segue uma figura ilustrando o autômato:

![Exemplo Autômato](/InsiraSeuAutomatoAqui/automatoexemplo.JPG)
