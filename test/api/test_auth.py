import requests
import pytest
from http import HTTPStatus

def test_user_registration_successful(base_url):
    """Test para verificar el registro exitoso de un usuario"""
    
    # Datos de prueba
    # Usar un timestamp para hacer el email único
    import time
    timestamp = int(time.time())
    test_data = {
        "email": f"albert{timestamp}@gmail.com",
        "password": "124789",
        "full_name": "Albert"
    }
    
    try:
        # Realizar la petición POST
        response = requests.post(
            url=f"{base_url}/auth/signup",
            json=test_data
        )
        
        # Verificar el código de estado
        assert response.status_code == HTTPStatus.CREATED, \
            f"Se esperaba código de estado 201, pero se recibió {response.status_code}"
        
        # Verificar que la respuesta es JSON
        response_data = response.json()
        
        # Verificaciones adicionales de la respuesta exitosa
        assert "id" in response_data, "La respuesta no contiene el campo 'id'"
        assert "email" in response_data, "La respuesta no contiene el campo 'email'"
        assert "full_name" in response_data, "La respuesta no contiene el campo 'full_name'"
        assert "role" in response_data, "La respuesta no contiene el campo 'role'"
        
        # Verificar que los datos coincidan con lo enviado
        assert response_data["email"] == test_data["email"], "El email en la respuesta no coincide"
        assert response_data["full_name"] == test_data["full_name"], "El nombre en la respuesta no coincide"
        
    except requests.RequestException as e:
        pytest.fail(f"La petición falló con el error: {str(e)}")
    except AssertionError as e:
        pytest.fail(f"La validación falló: {str(e)}")
        
def test_user_registration_invalid_email(base_url):
    """Test para verificar el manejo de email inválido"""
    
    # Datos de prueba con email inválido
    test_data = {
        "email": "invalid-email",
        "password": "124789",
        "full_name": "Albert"
    }
    
    try:
        response = requests.post(
            url=f"{base_url}/auth/signup",
            json=test_data
        )
        
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, \
            f"Se esperaba código 422, pero se recibió {response.status_code}"
            
        response_data = response.json()
        assert "detail" in response_data, "La respuesta no contiene el campo 'detail'"
        
    except requests.RequestException as e:
        pytest.fail(f"La petición falló con el error: {str(e)}")
