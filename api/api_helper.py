import requests
import time


class ApiHelper:
    """Helper class for making API requests"""

    URL_API = "https://cf-automation-airline-api.onrender.com/"

    def __init__(self, token=None):
        self.token = token
        self.headers = {}
        self.last_response = None
        if token:
            self.set_token(token)
    
    def set_token(self, token):
        self.token = token
        self.headers["Authorization"] = f"Bearer {token}"
    
    def make_request(self, endpoint, method="POST", data=None, use_form_data=False):
        """
        Realiza una petición HTTP

        :param endpoint: El endpoint de la API
        :param method: Método HTTP (GET, POST, etc)
        :param data: Datos a enviar
        :param use_form_data: Si True, envía los datos como form-data en lugar de JSON
        :return: Respuesta de la petición
        """
        url = f"{self.URL_API}{endpoint}"

        # Configurar los datos según el formato requerido
        request_kwargs = {
            "method": method,
            "url": url,
            "headers": self.headers.copy()
        }

        if data:
            if use_form_data:
                request_kwargs["data"] = data
                request_kwargs["headers"]["Content-Type"] = "application/x-www-form-urlencoded"
            else:
                request_kwargs["json"] = data

        self.last_response = requests.request(**request_kwargs)
        return self.last_response
    
    def get_last_response(self):
        
        return self.last_response
    
    def is_service_up(self):
        
        try:
            response = requests.get(self.URL_API)
            return response.status_code == 200
        except requests.RequestException:
            return False


if __name__ == "__main__":
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c3ItMWE5ZGFhNGYiLCJyb2xlIjoiYWRtaW4ifQ.hOxNwvee5q51zlMsKrCqO1bf8QL8fMLnwV8dzBNb0AE"
    api = ApiHelper(token)

    # Fixture: Verificar si el servicio está activo y medir tiempo de respuesta
    start_time = time.time()
    service_up = api.is_service_up()
    response_time = time.time() - start_time
    if service_up:
        print(f"El servicio API está funcionando correctamente. Tiempo de respuesta: {response_time:.3f} segundos")
        # Datos para el registro
        signup_data = {
            "email": "test@example.com",
            "password": "Test123!",
            "full_name": "Test User"
        }
        response = api.make_request("/auth/signup", data=signup_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    else:
        print(f"El servicio API no está disponible en este momento. Tiempo de respuesta: {response_time:.3f} segundos")
