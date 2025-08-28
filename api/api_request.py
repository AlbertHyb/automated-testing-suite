

import requests

URL = "https://cf-automation-airline-api.onrender.com/"
AUTH_LOGIN = "auth/login"
AUTH_SIGNUP = "/users/"
LIST_USERS = "/users?skip=0&limit=10"

admin_data = {
    "email": "admin@demo.com",
    "password": "Admin123"    
}

support_user_data = {
    "email": "laura.sanchez@airline.com",
    "password": "TAnvOCaTChil",
    "full_name": "Laura Sanchez",
    "role": "admin"
}

def login_as_admin():
    response = requests.post(
        url=f"{URL}{AUTH_LOGIN}",
        json=admin_data  # Cambiado de data a json
    )
    return response

def signup_support_user(support_data):
    response = requests.post(
        url=f"{URL}{AUTH_SIGNUP}",
        json=support_data, 
        headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c3ItZDhlNDc4ZDYiLCJyb2xlIjoiYWRtaW4ifQ.P4VrfixHuV-wZQPSBHkOhVeh7f68jD4SlnITbMSeRbw"}
    )
    return response

if __name__ == "__main__":
    # Intentar registrar el usuario de soporte
    response = signup_support_user(support_user_data)
    print("\nRegistro de usuario de soporte:")
    print(f"Status Code: {response.status_code}")
    print("Response JSON:")
    print(response.json()) 