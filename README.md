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

## Configuración en PyCharm

### Abrir el Proyecto
1. Abrir PyCharm
2. Seleccionar `File > Open`
3. Navegar hasta la carpeta del proyecto y seleccionar `automated-testing-suite`
4. Esperar a que PyCharm indexe el proyecto

### Configurar el Intérprete de Python
1. Ir a `File > Settings` (Windows/Linux) o `PyCharm > Preferences` (macOS)
2. Navegar a `Project: automated-testing-suite > Python Interpreter`
3. Hacer clic en el engranaje ⚙️ > `Add`
4. Seleccionar `Virtual Environment > Existing Environment`
5. Buscar el intérprete en:
   - Windows: `automated-testing-suite\venv\Scripts\python.exe`
   - Linux/Mac: `automated-testing-suite/venv/bin/python`
6. Hacer clic en `OK` para confirmar

### Configurar Test Runner
1. Ir a `File > Settings` (Windows/Linux) o `PyCharm > Preferences` (macOS)
2. Navegar a `Tools > Python Integrated Tools`
3. En la sección `Testing`, seleccionar `pytest` como Default test runner
4. Hacer clic en `OK` para confirmar

### Configurar Git en PyCharm
1. Ir a `VCS > Git > Remotes`
2. Verificar que el remote 'origin' apunte a nuestro repositorio
3. Para cambiar de rama:
   - Usar el widget de Git en la esquina inferior derecha
   - O `Git > Branches > New Branch`

### Ejecutar Tests
1. Click derecho en la carpeta `test`
2. Seleccionar `Run 'pytest in test'`
3. Para un archivo específico:
   - Click derecho en el archivo
   - Seleccionar `Run 'pytest in nombre_archivo.py'`

### Consejos Útiles
1. Usar `Shift + F10` para reejecutar el último test
2. `Alt + Enter` sobre una importación para instalar paquetes faltantes
3. `Ctrl + Alt + L` (Windows/Linux) o `Cmd + Alt + L` (macOS) para formatear código
4. `Shift + F6` para renombrar archivos y símbolos de forma segura

### Plugins Recomendados
1. `.env files support`
2. `Requirements`
3. `GitToolBox`
4. `Python Security`

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
