# App Gastos

Aplicación web para registrar, categorizar y visualizar gastos personales.

## Stack

- **Backend:** Django 5.2
- **Base de datos:** PostgreSQL 16
- **Frontend:** Django Templates + Bootstrap 5 (CDN)
- **Infraestructura:** Docker + Docker Compose

## Requisitos

- Docker + Docker Compose

## Inicio rápido

```bash
# 1. Clonar y entrar al proyecto
git clone <repo> && cd app-gastos

# 2. Iniciar servicios
docker compose up --build -d

# 3. (Primera vez) Seed de categorías
docker compose exec web python manage.py seed_categories

# 4. Abrir http://localhost:8000
```

## Desarrollo local

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Necesitas PostgreSQL corriendo localmente o modificar `DATABASES` en `settings.py` para usar SQLite.

## Variables de entorno

| Variable | Default | Descripción |
|---|---|---|
| `DB_NAME` | `expense_db` | Nombre BD |
| `DB_USER` | `expense_user` | Usuario BD |
| `DB_PASSWORD` | `expense_pass` | Contraseña BD |
| `DB_HOST` | `db` | Host BD |
| `DJANGO_SECRET_KEY` | _(dev key)_ | Secret key de Django |
| `DJANGO_DEBUG` | `True` | Modo debug |
| `CSRF_TRUSTED_ORIGINS` | `http://localhost:8000,...` | Orígenes permitidos (separados por coma) |
| `DJANGO_HTTPS` | `False` | `True` en producción para cookies seguras |

## Rutas

| Ruta | Descripción |
|---|---|
| `/` | Dashboard (requiere login) |
| `/usuarios/login/` | Iniciar sesión |
| `/usuarios/registro/` | Registrarse |
| `/transacciones/` | Lista de transacciones |
| `/transacciones/nueva/` | Crear transacción |
| `/transacciones/<id>/editar/` | Editar transacción |
| `/admin/` | Admin de Django |

## Estructura

```
app-gastos/
├── app/
│   ├── core/            # Dashboard
│   ├── users/           # Auth (login, registro, logout)
│   ├── transactions/    # CRUD de transacciones
│   └── categories/      # Modelo y seed de categorías
├── config/
│   ├── settings.py
│   └── urls.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Producción (AWS)

```yaml
# docker-compose.yml → environment:
  - CSRF_TRUSTED_ORIGINS=https://tudominio.com
  - DJANGO_HTTPS=True
  - DJANGO_DEBUG=False
  - DJANGO_SECRET_KEY=<generar clave>
```

Reemplazar el `command` del `web` por un servidor WSGI (Gunicorn/uWSGI) y agregar un proxy reverso (Nginx) para producción.
