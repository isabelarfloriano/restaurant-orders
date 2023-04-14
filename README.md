# Projeto Restaurant Orders! :hamburger::woman_cook:

"Restaurant Orders" é um projeto de melhoria desenvolvido para uma lanchonete fictícia chamada Pão na Chapa. A aplicação tem como objetivo aumentar as vendas e melhorar a gestão interna da lanchonete. Em um primeiro momento, o projeto irá gerar relatórios com informações sobre os pedidos e os clientes que frequentam a lanchonete, a fim de auxiliar o trabalho de uma agência de marketing. Já em um segundo momento, a aplicação irá focar no controle do estoque de ingredientes para garantir que o cardápio digital da lanchonete ofereça produtos disponíveis no estoque, evitando assim frustrações por parte dos clientes. Com a implementação do Projeto "Restaurant Orders", a lanchonete Pão na Chapa poderá oferecer um melhor atendimento e aumentar a satisfação dos seus clientes.

<details>
  <summary><strong>Objetivos de prática</strong></summary><br />
    <ul>
      <li>Trabalhar com `Hashmap` e `Dict`</li>
      <li>Trabalhar com `Set`</li>
    </ul>
</details>
<details>
  <summary><strong>Rodando Localmente a Aplicação</strong></summary><br />
  
  <p>Para executar a aplicação e os testes, siga os passos abaixo:</p>
  <ol>
    <li>Clone o projeto.</li>
    <li>Abra o terminal e navegue até a raiz do projeto.</li>
    <li>Crie o ambiente virtual com o comando <code>python3 -m venv .venv</code>.</li>
    <li>Ative o ambiente virtual com o comando <code>source .venv/bin/activate</code>.</li>
    <li>Instale as dependências com o comando <code>python3 -m pip install -r dev-requirements.txt</code>.</li>
    <li>Para gerar os relatórios via linha de comando, instale a dependência da linha de comando com o comando <code>pip install .</code>.</li>
    <li>Para executar todos os testes, execute o comando <code>python3 -m pytest</code> na raiz do projeto.</li>
  </ol>
</details>
<details>
  <summary><strong>Estrutura do Projeto</strong></summary><br />

  ```
.
├── data
│   ├──🔹 mkt_campaign.txt
│   ├──🔸 orders_1.csv
│   └──🔸 orders_2.csv
├── src
│   ├──🔹 analyze_log.py
│   ├──🔹 inventory_control.py
│   ├──🔸 main.py
│   └──🔹 track_orders.py
├── tests
│   └── 🔸__init__.py
├── 🔸dev-requirements.txt
├── 🔸pyproject.toml
├── 🔹README.md
├── 🔸requirements.txt
├── 🔸setup.cfg
└── 🔸setup.py
  
    Legenda:
  🔸Arquivos de propriedade intelectual da Trybe
  🔹Arquivos desenvolvidos por mim
  ```
</details>
<details>
  <summary><strong>Detalhes dos Desafios</strong></summary><br />
  <p>src/analyze_log.py</p>
    <ul>
      <li>A função lê os arquivos que contêm as informações dos pedidos realizados e gera o relatório solicitado.</li>
      <li>Podemos utilizar essa função para responder as seguintes perguntas:</li>
        <ul>
          <li>Qual o prato mais pedido por 'maria'?</li>
          <li>Quantas vezes 'arnaldo' pediu 'hamburguer'?</li>
          <li>Quais pratos 'joao' nunca pediu?</li>
          <li>Quais dias 'joao' nunca foi à lanchonete?</li>
        </ul>
    </ul>
    <details>
      <summary><b>Clique aqui para ver a saída correta da função considerando os exemplos acima.</b></summary>

```
hamburguer
1
{'pizza', 'coxinha', 'misto-quente'}
{'sabado', 'segunda-feira'}
```
  </details>
  <p>src/track_orders.py</p>
    <ul>
      <li>Classe que simula um sistema de registro contínuo das informações de pedidos</li>
      <li>Por meio dessa classe, é possível utilizar os seguintes métodos:</li>
        <ul>
          <li>`add_new_order` - o método registra um pedido na instância;</li>
          <li>`get_most_ordered_dish_per_customer` - o método retorna o prato mais pedido;</li>
          <li>`get_never_ordered_per_customer` - o método retorna o conjunto de pratos que a pessoa nunca pediu;</li>
          <li>`get_days_never_visited_per_customer` - o método retorna o conjunto de dias que a pessoa nunca visitou;</li>
          <li>`get_busiest_day` - o método retorna o dia mais movimentado;</li>
          <li>`get_least_busy_day` - o método retorna o dia menos movimentado;</li>
        </ul>
    </ul>
  <p>src/inventory_control.py</p>
    <ul>
      <li>Classe de gerenciamento do estoque de um estabelecimento</li>
      <li>Por meio dessa classe, é possível utilizar os seguintes métodos:</li>
        <ul>
          <li>`add_new_order` - se um pedido contém um prato que não possui ingredientes suficientes em estoque, o método retorna 'False' sem registrar o pedido. Caso contrário, o método adiciona o pedido ao sistema;</li>
          <li>`get_quantities_to_buy` - o método retorna a quantidade de ingredientes que precisam ser comprados;</li>
          <li>`get_available_dishes` - o método retorna todos os pratos que possuem ingredientes suficientes para seu preparo;</li>
        </ul>
    </ul>
</details>
