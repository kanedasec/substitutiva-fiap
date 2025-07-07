
# Plataforma de Venda de Veículos - FIAP

Este projeto implementa uma **plataforma de revenda de veículos automotores** baseada em **microsserviços**, utilizando **arquitetura hexagonal** e o padrão de transações distribuídas **SAGA (Orquestrador)**. A solução expõe APIs RESTful que poderão ser integradas futuramente por uma interface web (frontend).

---

## 🏗️ Arquitetura

A arquitetura é composta por múltiplos serviços independentes:

- `veiculos-service`: Gerencia cadastro, listagem, edição e reserva de veículos.
- `compradores-service`: Gerencia cadastro e verificação de compradores.
- `pagamentos-service`: Simula geração e confirmação de pagamentos.
- `vendas-orquestrador`: Orquestra o processo completo de uma venda de veículo com o padrão SAGA.

Cada serviço segue o padrão **Hexagonal (Ports & Adapters)** para isolamento de regras de negócio.

---

## 🔁 Orquestração SAGA

O fluxo de venda é controlado pelo serviço **vendas-orquestrador**, que coordena as etapas da transação distribuída:

1. Reserva do veículo
2. Verificação do comprador
3. Geração do código de pagamento
4. (Assíncrona) Confirmação de pagamento
5. Baixa do veículo no estoque

---

## 🚀 Como executar o projeto

Pré-requisitos:
- Python 3.11+
- Docker e Docker Compose (opcional, mas recomendado)

### ▶️ Iniciar os serviços

```bash
docker compose up --build
```

---

## 📚 Endpoints Principais

### Veículos (`localhost:8000`)
- `POST /veiculos`
- `GET /veiculos`
- `PATCH /veiculos/{id}`
- `PATCH /veiculos/{id}/reserva`

### Compradores (`localhost:8001`)
- `POST /compradores`
- `GET /compradores/{id}`

### Pagamentos (`localhost:8003`)
- `POST /pagamentos`
- `GET /pagamentos/{codigo}`
- `POST /pagamentos/{codigo}/confirmar`

### Vendas (Orquestrador) (`localhost:8002`)
- `POST /vendas`
- `POST /vendas/{id}/concluir`

---

## 🔐 Segurança de Dados

- Dados sensíveis de compradores são **criptografados** em repouso.
- A comunicação entre os microsserviços pode ser protegida por mTLS (não implementado nesta versão).
- O sistema é projetado para garantir **confidencialidade e integridade** no tratamento de dados pessoais.

---

## 📦 Organização de Código

Cada serviço segue a estrutura:

```
app/
├── adapters/          # Entrada e saída (ex: API REST, clients HTTP)
├── application/       # Casos de uso
├── domain/            # Regras de negócio (entidades)
├── infrastructure/    # Integração com serviços externos
├── main.py            # Inicialização do app
```

---

## 👨‍💻 Desenvolvido por

Projeto acadêmico desenvolvido por Vernon Simões como parte da Pós-Tech de Arquitetura de Software (FIAP).  

---
