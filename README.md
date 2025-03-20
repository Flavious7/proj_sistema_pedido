# Projeto Sistema de Gestão de Pedidos

Este repositório contém a documentação técnica, instruções de instalação e descrição detalhada dos endpoints e do fluxo desenvolvido com WSO2 Micro Integrator para o projeto **Sistema de Gestão de Pedidos**.

---

## 📋 Instruções de Instalação e Uso

Siga os passos abaixo para executar o projeto localmente:

### Pré-requisitos
- Docker
- Docker Compose

### Execução

1. **Navegue até à pasta do projeto:**

```bash
cd "\sistemas pedidos-Beta1\sistemas pedidos\backend"
```

2. **Inicialize os containers Docker:**

```bash
docker-compose up
```

3. **Aguarde que os serviços sejam inicializados.** Após isso:

- Backend estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- WSO2 Micro Integrator estará disponível em: [http://localhost:8290](http://localhost:8290)

Agora pode utilizar o Insomnia ou ferramentas semelhantes para realizar requisições HTTP aos endpoints descritos abaixo.

---

## 🔗 Endpoints Utilizados no Insomnia

### 📌 Empresa:
- `GET` **Listar empresas**: `http://127.0.0.1:8000/app/empresa`
- `GET` **Detalhes da empresa por ID**: `http://127.0.0.1:8000/app/empresa/{id}`
- `POST` **Criar nova empresa**: `http://127.0.0.1:8000/app/empresa/create`
- `PUT` **Atualizar empresa existente**: `http://127.0.0.1:8000/app/empresa/update/{id}`
- `DELETE` **Remover empresa**: `http://127.0.0.1:8000/app/empresa/delete/{id}`

### 📌 Pedido:
- `GET` **Listar todos os pedidos**: `http://127.0.0.1:8000/app/pedido`
- `GET` **Detalhes do pedido por ID**: `http://127.0.0.1:8000/app/pedido/{id}`
- `POST` **Criar novo pedido**: `http://127.0.0.1:8000/app/pedido/create`
- `PUT` **Atualizar pedido existente**: `http://127.0.0.1:8000/app/pedido/update/{id}`
- `DELETE` **Remover pedido**: `http://127.0.0.1:8000/app/pedido/delete/{id}`

### 📌 WSO2 Micro Integrator:
- `POST` **Validar Pedido**: `http://localhost:8290/validarpedido`

---

## ⚙️ Fluxo WSO2 Micro Integrator

O fluxo criado no **Dashboard do WSO2 Micro Integrator** funciona da seguinte forma:

1. O backend envia uma requisição HTTP (`/validarpedido`) com os detalhes do pedido.
2. O WSO2 MI executa:
   - **Filtragem por valor:**
     - Valor inferior a **1000€** → Pedido aprovado automaticamente.
     - Valor superior a **1000€** → Pedido fica pendente para aprovação manual (integração simulada com sistema externo).

   - **Resposta:**
     - Retorna uma resposta HTTP ao backend com o estado atualizado (**APROVADO** ou **PENDENTE**).

3. O fluxo desenhado no Dashboard é exportado como ficheiro XML e integrado diretamente no projeto, sendo carregado automaticamente pelo Docker Compose (volume mounts) no container do WSO2 MI durante o arranque.

Desta forma, garantimos uma integração robusta, escalável e eficiente entre o Backend, o WSO2 Micro Integrator e a base de dados PostgreSQL, atendendo integralmente aos requisitos do projeto.
