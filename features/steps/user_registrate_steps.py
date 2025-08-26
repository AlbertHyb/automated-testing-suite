from behave import given, when, then
from pages.api.api_helper import ApiHelper

@given('el servicio de autenticacionesta disponible')
def step_impl(context):
    # Inicializar el helper de API
    context.api = ApiHelper()
    
    # Verificar que el servicio está disponible
    is_available = context.api.is_service_up()
    
    # Si el servicio no está disponible, el test fallará con un mensaje claro
    assert is_available, "El servicio de autenticación no está disponible o no responde"
    
    # Guardar el estado inicial para usar en otros steps
    context.api_available = True
@when('Envío correo electrónico, contraseña y nombre válidos a /api/auth/login')
def step_impl(context):
    # Datos para el login
    login_data = {
        "email": "test@example.com",
        "password": "Test123!"
    }
    
    # Realizar la petición de login
    # Usar el api helper ya inicializado en el paso Given
    context.response = context.api.make_request(
        endpoint="/auth/login",
        method="POST",
        data=login_data
    )

@then('deberia recibir un 201')
def step_impl(context):
    # Verificar que el código de estado sea 201 (Created)
    assert context.response.status_code == 201, \
        f"Se esperaba el código de estado 201 pero se recibió {context.response.status_code}"
    
    # Verificar que la respuesta sea JSON válido
    response_data = context.response.json()
    
    # Verificar que la respuesta contenga un mensaje de éxito
    assert "message" in response_data, "La respuesta no contiene el campo 'message'"
    assert "created successfully" in response_data["message"].lower(), \
        f"Mensaje de éxito no encontrado en la respuesta: {response_data['message']}" 


@when('Envio correo electronico invalido a /api/auth/login')
def step_impl(context):
    login_data = {
        "email": "test@example",
        "password": "Test123!"
    }

@then('deberia recibir un 422')
def step_impl(context):

    # Verificar que el código de estado sea 422 (Created)
    assert context.response.status_code == 422, \
        f"Se esperaba el código de estado 422 pero se recibió {context.response.status_code}"
    
    # Verificar que la respuesta sea JSON válido
    response_data = context.response.json()
    
    # Verificar que la respuesta contenga un mensaje de éxito
    assert "message" in response_data, "La respuesta no contiene el campo 'message'"
    assert any(keyword in response_data["message"].lower() for keyword in ["error", "invalid", "required", "validation"]), \
        f"Mensaje de error no encontrado en la respuesta: {response_data['message']}"

@when('Envio  una contraseña erronea a /api/auth/login')
def step_impl(context):
    login_data = {
        "email": "test@example",
        "password": "Test123!"
    }

@then('deberia recibir un 422')
def step_impl(context):

    # Verificar que el código de estado sea 422 (Created)
    assert context.response.status_code == 422, \
        f"Se esperaba el código de estado 422 pero se recibió {context.response.status_code}"
    
    # Verificar que la respuesta sea JSON válido
    response_data = context.response.json()
    
    # Verificar que la respuesta contenga un mensaje de éxito
    assert "message" in response_data, "La respuesta no contiene el campo 'message'"
    assert any(keyword in response_data["message"].lower() for keyword in ["error", "invalid", "required", "validation"]), \
        f"Mensaje de error no encontrado en la respuesta: {response_data['message']}"           

@when('Envio un correo ya existente a /api/auth/login')
def step_impl(context):
    login_data = {
        "email": "test@example",
        "password": "Test123!"
    }


@then('deberia recibir un 400')
def step_impl(context):
    # Verificar que el código de estado sea 400 (Bad Request)
    assert context.response.status_code == 400, \
        f"Se esperaba el código de estado 400 pero se recibió {context.response.status_code}"
    
    # Verificar que la respuesta sea JSON válido
    response_data = context.response.json()
    
    # Verificar que la respuesta contenga un mensaje de error
    assert "message" in response_data, "La respuesta no contiene el campo 'message'"
    assert any(keyword in response_data["message"].lower() for keyword in ["error", "invalid", "required", "validation"]), \
        f"Mensaje de error no encontrado en la respuesta: {response_data['message']}"

@when('Envio un nombre vacio a /api/auth/login')
def step_impl(context):
    login_data = {
        "email": "test@example",
        "password": "Test123!"
    }  

@then('deberia recibir un 422')
def step_impl(context):

    # Verificar que el código de estado sea 422 (Created)
    assert context.response.status_code == 422, \
        f"Se esperaba el código de estado 422 pero se recibió {context.response.status_code}"
    
    # Verificar que la respuesta sea JSON válido
    response_data = context.response.json()
    
    # Verificar que la respuesta contenga un mensaje de éxito
    assert "message" in response_data, "La respuesta no contiene el campo 'message'"
    assert any(keyword in response_data["message"].lower() for keyword in ["error", "invalid", "required", "validation"]), \
        f"Mensaje de error no encontrado en la respuesta: {response_data['message']}"    


