# Estructura sugerida del proyecto
automated-testing-suite/
├── src/                      # Código fuente
│   ├── api/                 # Capa de API
│   │   ├── helpers/        # Helpers de API
│   │   └── schemas/        # Esquemas JSON
│   ├── ui/                 # Capa de UI
│   │   ├── pages/         # Page Objects
│   │   └── components/    # Componentes reutilizables
│   └── utils/             # Utilidades comunes
├── tests/                   # Tests separados por tipo
│   ├── api/               # Pruebas de API
│   │   ├── auth/         # Pruebas de autenticación
│   │   └── airports/     # Pruebas de aeropuertos
│   └── ui/               # Pruebas de UI
├── config/                  # Configuraciones
│   ├── environments/      # Configuraciones por ambiente
│   └── settings/         # Configuraciones generales
├── fixtures/               # Fixtures centralizados
│   ├── api/              # Fixtures de API
│   └── ui/               # Fixtures de UI
├── reports/                # Reportes de pruebas
└── docs/                   # Documentación

