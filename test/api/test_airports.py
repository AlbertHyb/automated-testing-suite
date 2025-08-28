import pytest
import requests
from jsonschema import validate
from http import HTTPStatus
from config.settings import Config
from config.constants import ENDPOINTS

airport_schema = {
    "type": "object",
    "required": ["iata_code", "city", "country"],
    "properties": {
        "iata_code": {
            "type": "string",
            "minLength": 3,
            "maxLength": 3
        },
        "city": {
            "type": "string"
        },
        "country": {
            "type": "string"
        }
    },
    "additionalProperties": False
}

def test_create_airport_schema(static_airport):
    """Test para verificar que la respuesta del endpoint de creación de aeropuerto
    cumple con el esquema JSON esperado"""
    
    try:
        validate(instance=static_airport, schema=airport_schema)
    except Exception as e:
        pytest.fail(f"El esquema JSON no es válido: {str(e)}")

def test_get_all_airports(static_airport, auth_headers):
    """Test para verificar la obtención de todos los aeropuertos"""
    response = requests.get(
        f"{Config.get_base_url()}{ENDPOINTS['AIRPORTS']}",
        headers=auth_headers,
        timeout=Config.get_request_timeout()
    )
    
    # Verificar el código de estado
    assert response.status_code == HTTPStatus.OK
    
    # Verificar que la respuesta es una lista no vacía
    airports = response.json()
    assert isinstance(airports, list), "La respuesta debería ser una lista"
    assert len(airports) > 0, "La lista de aeropuertos no debería estar vacía"
    
    # Verificar que cada aeropuerto cumple con el esquema
    for airport in airports:
        validate(instance=airport, schema=airport_schema)        