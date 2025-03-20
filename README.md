# proj_sistema_pedido
Documentação do Projeto - Endpoints e Fluxo WSO2 MI
Instruções de Instalação e Uso

Para instalar e executar o projeto, siga estes passos:

1. Certifique-se de que tem o Docker e Docker Compose instalados na sua máquina.

2. Navegue até à pasta do projeto:
   cd \sistemas pedidos-Beta1\sistemas pedidos\backend

3. Inicialize os containers Docker com o comando:
   docker-compose up

4. Após os containers serem inicializados com sucesso:
   - Backend estará disponível em: http://127.0.0.1:8000
   - WSO2 Micro Integrator estará disponível em: http://localhost:8290

Agora, pode utilizar o Insomnia ou outra ferramenta similar para realizar requisições HTTP aos endpoints descritos acima.
Endpoints Utilizados no Insomnia

Empresa:
GET - Listar empresas: http://127.0.0.1:8000/app/empresa
GET - Obter detalhes da empresa por ID: http://127.0.0.1:8000/app/empresa/{id}
POST - Criar nova empresa: http://127.0.0.1:8000/app/empresa/create
PUT - Atualizar empresa existente: http://127.0.0.1:8000/app/empresa/update/{id}
DELETE - Remover empresa: http://127.0.0.1:8000/app/empresa/delete/{id}

Pedido:
GET - Listar todos os pedidos: http://127.0.0.1:8000/app/pedido
GET - Obter detalhes do pedido por ID: http://127.0.0.1:8000/app/pedido/{id}
POST - Criar novo pedido: http://127.0.0.1:8000/app/pedido/create
PUT - Atualizar pedido existente: http://127.0.0.1:8000/app/pedido/update/{id}
DELETE - Remover pedido: http://127.0.0.1:8000/app/pedido/delete/{id}

WSO2 Micro Integrator:
POST - Validar Pedido (WSO2): http://localhost:8290/validarpedido


Fluxo criado no WSO2 Micro Integrator

Utilizámos o Dashboard do WSO2 Micro Integrator para criar o seguinte fluxo:

1. O backend envia uma requisição HTTP (endpoint acima: /validarpedido) contendo as informações de um pedido.
2. O WSO2 MI recebe essa requisição e executa as seguintes etapas no fluxo criado:
   - Filtragem por valor:
     - Se o valor for inferior a 1000€, o pedido é aprovado automaticamente.
     - Se o valor exceder 1000€, o pedido fica pendente para aprovação manual, simulando a integração com um sistema externo.

   - Resposta:
     - Após a decisão do fluxo, o WSO2 MI retorna uma resposta HTTP ao backend contendo o novo estado (APROVADO ou PENDENTE).

3. Após desenharmos esse fluxo visualmente no Dashboard do WSO2 MI, exportámos a configuração em formato XML e incluímo-la diretamente no nosso projeto. Em seguida, utilizámos a funcionalidade de volume mounts do Docker Compose para carregar automaticamente o ficheiro XML dentro do container do WSO2 MI durante a sua inicialização.

Deste modo, garantimos uma integração simples, clara e funcional entre o Backend, WSO2 MI e a base de dados PostgreSQL, conforme solicitado pelo projeto.

