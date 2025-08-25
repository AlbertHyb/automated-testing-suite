# Automated Testing Suite

Suite de pruebas automatizadas para pruebas end to end, pruebas críticas, así como pruebas de API.

## Configuración del Repositorio

### Clonar el Repositorio
```bash
# Clonar el repositorio
git clone https://github.com/AlbertHyb/automated-testing-suite.git

# Entrar al directorio del proyecto
cd automated-testing-suite
```

### Configuración Inicial
```bash
# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate  # En Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Flujo de Trabajo con Ramas

El proyecto sigue un modelo de ramificación basado en GitFlow:

### Ramas Principales
- `main`: Rama principal que contiene código estable y pruebas verificadas
- `develop`: Rama de desarrollo donde se integran nuevas características

### Ramas de Características
Para trabajar en nuevas características o conjuntos de pruebas:

1. Crear rama desde `develop`:
```bash
git checkout develop
git pull origin develop
git checkout -b feature/nombre-caracteristica
```

2. Trabajar en la nueva característica y hacer commits:
```bash
git add .
git commit -m "Descripción del cambio"
```

3. Subir cambios al repositorio remoto:
```bash
git push origin feature/nombre-caracteristica
```

4. Cuando la característica esté lista, crear un Pull Request a `develop`

### Convenciones de Nombres para Ramas
- `feature/*`: Para nuevas características o conjuntos de pruebas
- `fix/*`: Para correcciones de pruebas existentes
- `hotfix/*`: Para correcciones urgentes en producción
- `test/*`: Para experimentar con nuevos frameworks o enfoques de pruebas

### Buenas Prácticas
1. Mantener las ramas actualizadas con `develop`:
```bash
git checkout develop
git pull origin develop
git checkout tu-rama
git merge develop
```

2. Hacer commits frecuentes y descriptivos
3. Crear Pull Requests para revisión de código
4. Eliminar ramas después de integrarlas

## Estructura del Proyecto
```
automated-testing-suite/
├── api/          # Pruebas de API
├── config/       # Configuraciones y variables de entorno
├── pages/        # Page Objects para pruebas UI
├── reports/      # Reportes de pruebas
├── test/         # Suites de pruebas
└── utils/        # Utilidades y helpers
```
