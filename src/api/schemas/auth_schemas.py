"""Esquemas de autenticación centralizados"""

# Esquemas de login
login_success_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "access_token": {"type": "string"},
        "token_type": {"type": "string", "enum": ["bearer", "Bearer"]},
        "expires_in": {"type": "integer", "minimum": 1}
    },
    "required": ["access_token", "token_type"]
}

# Esquemas de registro
signup_success_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "string", "pattern": "^usr-[a-zA-Z0-9]+$"},
        "email": {"type": "string", "format": "email"},
        "full_name": {"type": "string", "minLength": 1},
        "role": {"type": "string", "enum": ["passenger", "admin"]}
    },
    "required": ["id", "email", "full_name", "role"]
}

# Esquema común para errores de validación
validation_error_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "detail": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "loc": {"type": "array", "items": {"type": "string"}},
                    "msg": {"type": "string"},
                    "type": {"type": "string"}
                },
                "required": ["loc", "msg", "type"]
            }
        }
    },
    "required": ["detail"]
}
