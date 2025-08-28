import os
import json
import requests
import pytest
from typing import Dict
from dotenv import load_dotenv

import random
import string
from faker import Faker

# Cargar variables de entorno
load_dotenv()

BASE_URL = "https://cf-automation-airline-api.onrender.com"

@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL

"""Fixture que proporciona el token de administrador"""
@pytest.fixture(scope="session")
def admin_token() -> str:
    username = os.getenv("ADMIN_USER") 
    password = os.getenv("ADMIN_PASS")
    print(f"\nUsername: {username}")
    print(f"Password: {password}")
    
    login_data = {
        "username": username,
        "password": password
    }
    
    try:
        print("\nIntentando login...")
        print(f"Login data: {login_data}")  # Para ver qué datos se están enviando
        response = requests.post(
            f"{BASE_URL}/auth/login",
            data=login_data
        )
        print(f"Login response ({response.status_code}): {response.text}")
        
        # Verificar respuesta
        response.raise_for_status()
        token = response.json().get("access_token")
        
        if not token:
            pytest.fail("No se encontró el token en la respuesta")
            
        return token
        
    except requests.RequestException as e:
        pytest.fail(f"Error al obtener el token: {str(e)}")
    except json.JSONDecodeError as e:
        pytest.fail(f"Error al decodificar la respuesta: {str(e)}")
        

"""Fixture que proporciona los headers de autenticación"""
@pytest.fixture(scope="session")
def auth_headers(admin_token) -> Dict[str, str]:
    
    return {"Authorization": f"Bearer {admin_token}"}

@pytest.fixture(scope="session")
def airports_data() -> dict:
    """Fixture que proporciona datos estáticos para pruebas de aeropuertos"""
    return {
        "valid_airports": [
            {
                "iata_code": "SCL",
                "city": "Santiago",
                "country": "CL"
            },
            {
                "iata_code": "LIM",
                "city": "Lima",
                "country": "PE"
            },
            {
                "iata_code": "BOG",
                "city": "Bogota",
                "country": "CO"
            },
            {
                "iata_code": "MEX",
                "city": "Ciudad de Mexico",
                "country": "MX"
            }
        ],
        "invalid_airports": [
            {
                "iata_code": "INVALID",  # Más de 3 caracteres
                "city": "Invalid City",
                "country": "XX"
            },
            {
                "iata_code": "12",  # Menos de 3 caracteres
                "city": "Invalid City",
                "country": "XX"
            },
            {
                "iata_code": "123",  # Números en lugar de letras
                "city": "Invalid City",
                "country": "XX"
            }
        ],
        "update_data": {
            "city": "Ciudad Actualizada",
            "country": "AR"
        }
    }

@pytest.fixture
def static_airport(auth_headers, airports_data):
    """Fixture que proporciona un aeropuerto de prueba con datos estáticos y lo limpia después"""
    AIRPORTS_ENDPOINT = "/airports"
    
    # Usar el primer aeropuerto válido de nuestros datos estáticos
    airport_data = airports_data["valid_airports"][0]

    response = requests.post(
        f"{BASE_URL}{AIRPORTS_ENDPOINT}", 
        json=airport_data, 
        headers=auth_headers, 
        timeout=5
    )
    response.raise_for_status()
    airport_response = response.json()
    
    yield airport_response
    
    # Limpieza: eliminar el aeropuerto creado
    requests.delete(
        f"{BASE_URL}{AIRPORTS_ENDPOINT}/{airport_response['iata_code']}", 
        headers=auth_headers, 
        timeout=5
    )

@pytest.fixture
def dynamic_airport(auth_headers):
    """Fixture que proporciona un aeropuerto de prueba con datos dinámicos y lo limpia después"""
    fake = Faker()
    AIRPORTS_ENDPOINT = "/airports"
    
    airport_data = {
        "iata_code": "".join(random.choices(string.ascii_uppercase, k=3)),
        "city": fake.city(),
        "country": fake.country_code()
    }

    response = requests.post(
        f"{BASE_URL}{AIRPORTS_ENDPOINT}", 
        json=airport_data, 
        headers=auth_headers, 
        timeout=5
    )
    response.raise_for_status()
    airport_response = response.json()
    
    yield airport_response
    
    # Limpieza: eliminar el aeropuerto creado
    requests.delete(
        f"{BASE_URL}{AIRPORTS_ENDPOINT}/{airport_response['iata_code']}", 
        headers=auth_headers, 
        timeout=5
    )






