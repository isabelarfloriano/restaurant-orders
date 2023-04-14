# Projeto Restaurant Orders! :hamburger::woman_cook:

"Restaurant Orders" é um projeto de melhoria desenvolvido para uma lanchonete fictícia chamada Pão na Chapa. A aplicação tem como objetivo aumentar as vendas e melhorar a gestão interna da lanchonete. Em um primeiro momento, o projeto irá gerar relatórios com informações sobre os pedidos e os clientes que frequentam a lanchonete, a fim de auxiliar o trabalho de uma agência de marketing. Já em um segundo momento, a aplicação irá focar no controle do estoque de ingredientes para garantir que o cardápio digital da lanchonete ofereça produtos disponíveis no estoque, evitando assim frustrações por parte dos clientes. Com a implementação do Projeto "Restaurant Orders", a lanchonete Pão na Chapa fictícia espera oferecer um melhor atendimento e aumentar a satisfação dos seus clientes.

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
    </ul>	
  <p>src/track_orders.py</p>
    <ul>
      <li>Classe que simula um sistema de registro contínuo das informações de pedidos</li>
    </ul>
  <p>src/inventory_control.py</p>
    <ul>
      <li>Classe de gerenciamento do estoque de um estabelecimento</li>
    </ul>
</details>
