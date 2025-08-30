# Automated Testing Suite

## Descripción
Suite de pruebas automatizadas para validar la funcionalidad de la API de autenticación y aeropuertos. Incluye pruebas de:
- Autenticación (login/signup)
- Gestión de aeropuertos
- Validaciones de esquemas JSON

## Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Acceso a la API (cf-automation-airline-api.onrender.com)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tuusuario/automated-testing-suite.git
cd automated-testing-suite
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar .env con tus credenciales
```

## Estructura del Proyecto
```
automated-testing-suite/
├── api/                    # Helpers y utilidades para API
├── config/                 # Configuraciones
├── test/
│   ├── api/               # Pruebas de API
│   │   ├── schemas/       # Esquemas JSON
│   │   ├── auth_login.py  # Pruebas de login
│   │   ├── auth_signup.py # Pruebas de registro
│   │   └── test_airports.py
│   └── ui/                # Pruebas de UI (si aplica)
├── utils/                 # Utilidades generales
└── requirements.txt       # Dependencias
```

## Ejecución de Pruebas

### Todas las pruebas:
```bash
pytest
```

### Pruebas específicas:
```bash
# Pruebas de autenticación
pytest test/api/auth_login.py -v
pytest test/api/auth_signup.py -v

# Pruebas de aeropuertos
pytest test/api/test_airports.py -v
```

### Generar reporte HTML:
```bash
pytest --html=reports/report.html
```

## Escenarios Cubiertos

### Autenticación
- Login exitoso
- Credenciales inválidas
- Campos faltantes
- Formatos inválidos

### Aeropuertos
- Creación exitosa
- Validación de códigos IATA
- Manejo de duplicados
- Actualizaciones y eliminaciones

## Contribución
1. Fork el repositorio
2. Crear rama feature: `git checkout -b feature/nueva-caracteristica`
3. Commit cambios: `git commit -am 'Añadir nueva característica'`
4. Push a la rama: `git push origin feature/nueva-caracteristica`
5. Crear Pull Request

## Licencia
MIT License - ver [LICENSE](LICENSE) para más detalles.
