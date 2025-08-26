import requests


class ApiHelper:
    """Helper class for making API requests"""

    URL_API = "https://cf-automation-airline-api.onrender.com/"

    def __init__(self, token=None):
        """
        Inicializa el helper con un token opcional
        Args:
            token (str, optional): Token de autorización
        """
        self.token = token
        self.headers = {}
        self.last_response = None
        if token:
            self.set_token(token)
    
    def set_token(self, token):
        """
        Actualiza el token de autorización
        Args:
            token (str): Nuevo token
        """
        self.token = token
        self.headers["Authorization"] = f"Bearer {token}"
    
    def make_request(self, endpoint, method="POST", data=None):
        """
        Realiza una petición HTTP
        Args:
            endpoint (str): Endpoint de la API
            method (str): Método HTTP (GET, POST, etc)
            data (dict): Datos para enviar en el cuerpo de la petición
        Returns:
            requests.Response: Objeto de respuesta
        """
        url = f"{self.URL_API}{endpoint}"
        self.last_response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            json=data
        )
        return self.last_response
    
    def get_last_response(self):
        """
        Obtiene la última respuesta recibida
        Returns:
            requests.Response: Última respuesta recibida
        """
        return self.last_response
    
    def is_service_up(self):
        """
        Verifica si el servicio API está funcionando.
        Returns:
            bool: True si el servicio responde, False si no.
        """
        try:
            response = requests.get(self.URL_API)
            return response.status_code == 200
        except requests.RequestException:
            return False


if __name__ == "__main__":
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c3ItMWE5ZGFhNGYiLCJyb2xlIjoiYWRtaW4ifQ.hOxNwvee5q51zlMsKrCqO1bf8QL8fMLnwV8dzBNb0AE"
    api = ApiHelper(token)
    
    # Verificar si el servicio está activo
    if api.is_service_up():
        print("El servicio API está funcionando correctamente")
        
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
        print("El servicio API no está disponible en este momento")            