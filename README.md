# Parking Service API

API REST para gerenciamento de estacionamento, desenvolvida com Django e Django REST Framework.

## 🚀 Tecnologias

- **Python 3.13**
- **Django 6.1**
- **Django REST Framework 3.18**
- **PostgreSQL 15**
- **RabbitMQ 4.2** (message broker)
- **Celery 5.6** (processamento assíncrono)
- **JWT** (autenticação via `djangorestframework-simplejwt`)
- **DRF Spectacular** (documentação OpenAPI/Swagger)
- **Django RQL** (filtros avançados via query language)

## 📋 Funcionalidades

### Módulos Principais

| App | Descrição |
|-----|-----------|
| **authentication** | Autenticação e autorização (JWT) |
| **customers** | Gestão de clientes |
| **vehicles** | Gestão de veículos e tipos de veículos |
| **parking** | Controle de vagas e registros de estacionamento |

### Entidades

- **Customer**: Clientes do estacionamento (nome, CPF, telefone)
- **VehicleType**: Tipos de veículos (carro, moto, caminhão, etc.)
- **Vehicle**: Veículos cadastrados (placa, marca, modelo, cor, tipo, proprietário)
- **ParkingSpot**: Vagas de estacionamento (número, status ocupado/livre)
- **ParkingRecord**: Registros de entrada/saída de veículos nas vagas

## 🔧 Pré-requisitos

- Docker e Docker Compose
- Ou: Python 3.13+, PostgreSQL 15+, RabbitMQ 4.2+

## 🐳 Executando com Docker (Recomendado)

```bash
cd parking_service
docker-compose up --build
```

A API estará disponível em: **http://localhost:8000**

Serviços incluídos:
- **API**: http://localhost:8000
- **Admin Django**: http://localhost:8000/admin
- **Documentação Swagger**: http://localhost:8000/api/v1/docs/
- **Documentação Redoc**: http://localhost:8000/api/v1/redoc/
- **RabbitMQ Management**: http://localhost:15672 (guest/guest)
- **PostgreSQL**: localhost:5432 (postgres/postgres)

## 💻 Executando Localmente (Desenvolvimento)

```bash
cd parking_service

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente (criar .env)
# Ver .env.example para referência

# Executar migrações
python manage.py migrate

# Criar superusuário (opcional)
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver

# Em outro terminal - iniciar Celery worker
celery -A core worker -l INFO
```

## 📚 Documentação da API

- **Swagger UI**: `/api/v1/schema/swagger-ui/`
- **ReDoc**: `/api/v1/schema/redoc/`
- **Schema OpenAPI**: `/api/v1/schema/`

## 🔐 Autenticação

A API utiliza **JWT (JSON Web Tokens)**:

```bash
# Obter token
curl -X POST http://localhost:8000/api/v1/authentication/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "seu_usuario", "password": "sua_senha"}'

# Usar token
curl -H "Authorization: Bearer SEU_TOKEN" http://localhost:8000/api/vehicles/
```

## 📡 Endpoints Principais

### Autenticação
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/auth/token/` | Obter token JWT |
| POST | `/api/auth/token/refresh/` | Renovar token |

### Clientes (`/api/customers/`)
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/customers/` | Listar clientes |
| POST | `/api/customers/` | Criar cliente |
| GET | `/api/customers/{id}/` | Detalhar cliente |
| PUT/PATCH | `/api/customers/{id}/` | Atualizar cliente |
| DELETE | `/api/customers/{id}/` | Deletar cliente |

### Veículos (`/api/vehicles/`)
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/vehicles/` | Listar veículos |
| POST | `/api/vehicles/` | Cadastrar veículo |
| GET | `/api/vehicles/{id}/` | Detalhar veículo |
| PUT/PATCH | `/api/vehicles/{id}/` | Atualizar veículo |
| DELETE | `/api/vehicles/{id}/` | Remover veículo |
| GET | `/api/vehicle-types/` | Listar tipos de veículo |

### Estacionamento (`/api/parking/`)
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/parking/spots/` | Listar vagas |
| POST | `/api/parking/spots/` | Criar vaga |
| GET | `/api/parking/records/` | Listar registros |
| POST | `/api/parking/records/` | Registrar entrada |
| PATCH | `/api/parking/records/{id}/exit/` | Registrar saída |

## 🔍 Filtros Avançados (RQL)

A API utiliza a biblioteca **django-rql** para permitir consultas e filtragens avançadas dos recursos, utilizando a linguagem **RQL (Resource Query Language)**.

```bash
# Buscar veículos pela placa
GET /api/vehicles/?eq(licence_plate,ABC1234)

# Buscar clientes pelo nome, ignorando maiúsculas e minúsculas
GET /api/customers/?ilike(name,*João*)

# Buscar vagas desocupadas
GET /api/parking/spots/?eq(is_occuped,false)

# Buscar veículos com uma das placas informadas
GET /api/vehicles/?in(licence_plate,(ABC1234,XYZ5678))

# Combinar condições: veículos de uma marca específica
# e com ano de fabricação maior ou igual a 2020
GET /api/vehicles/?and(eq(brand,Toyota),ge(year,2020))

# Ordenar veículos pela data de criação (mais recentes primeiro)
GET /api/vehicles/?ordering(-created_at)

# Paginar resultados (20 registros a partir do deslocamento 20)
GET /api/vehicles/?limit=20&offset=20
```

## 🧪 Testes

```bash
# Executar todos os testes
python manage.py test

# Com coverage
coverage run --source='.' manage.py test
coverage report
```

## 📁 Estrutura do Projeto

```
parking_service/
├── core/                 # Configurações principais do Django
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   └── permissions.py
├── authentication/       # App de autenticação
├── customers/           # App de clientes
├── vehicles/            # App de veículos
│   ├── models.py        # Vehicle, VehicleType
│   ├── views.py
│   ├── serializers.py
│   ├── tasks.py         # Tarefas Celery
│   ├── signals.py       # Signals Django
│   └── filters.py       # Filtros RQL
├── parking/             # App de estacionamento
│   ├── models.py        # ParkingSpot, ParkingRecord
│   ├── views.py
│   ├── serializers.py
│   └── signals.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── manage.py
```


## 📝 Licença

Este projeto é de uso interno/educacional.

