# QA Project - Urban Routes

## Descripción

Proyecto de automatización de pruebas end-to-end para la aplicación web **Urban Routes** (simulador de pedido de taxi tipo Uber/Cabify). Las pruebas cubren el flujo completo de solicitud de un viaje: configuración de dirección, selección de tarifa Comfort, registro de número de teléfono con verificación por SMS, registro de tarjeta de crédito, mensaje para el conductor, solicitud de manta y pañuelos, y pedido de helados, hasta la confirmación del pedido con el modal de búsqueda de automóvil.

## Tecnologías y técnicas utilizadas

- **Python 3**
- **Selenium WebDriver** para automatización del navegador (Chrome)
- **pytest** como framework de pruebas
- **Page Object Model (POM)**: separación de localizadores y métodos de interacción (`UrbanRoutesPage`) de la lógica de las pruebas (`TestUrbanRoutes`)
- Patrón de métodos **SETTER / CLICKER / READER / GETTER** para interactuar y verificar elementos del DOM
- **WebDriverWait** y **expected_conditions (EC)** para esperas explícitas
- Interceptación de logs de red del navegador (`goog:loggingPrefs` / Performance log) para extraer el código de confirmación SMS mediante `retrieve_phone_code()`
- Uso de `Keys.TAB` para forzar el evento `blur` en el campo CVV y habilitar el botón de agregar tarjeta

## Estructura del proyecto
qa-project-Urban-Routes-es/
├── data/
│ └── data.py # Datos de prueba (direcciones, teléfono, tarjeta, mensaje)
├── pages/
│ └── urban_routes_page.py # Localizadores y métodos (Page Object)
├── test/
│ └── test_urban_routes.py # Casos de prueba
├── utilis/
│ └── retrieve_code.py # Función para obtener el código SMS (no modificar)
└── README.md


## Cómo ejecutar las pruebas

1. Clonar el repositorio:
```bash
   git clone <url-del-repositorio>
   cd qa-project-Urban-Routes-es
```

2. Crear y activar un entorno virtual:
```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS/Linux
```

3. Instalar las dependencias:
```bash
   pip install selenium pytest
```

4. Asegurarse de tener **Google Chrome** y **ChromeDriver** instalados, con versiones compatibles entre sí, y que `chromedriver` esté en el `PATH`.

5. Ejecutar las pruebas con pytest desde la raíz del proyecto:
```bash
   pytest test/test_urban_routes.py -v
```