from tests.test_register_and_login import login_user

USER_DATA_SCHEME = {
    "type" : "object",
    "properties" : {
        "id": {"type": "number"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"}
    },
    "required" : ["id", "email", "first_name","last_name","avatar" ]
}

RESOURCE_DATA_SCHEME = {
    "type" : "object",
    "properties" : {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "year": {"type": "number"},
        "color": {"type": "string"},
        "pantone_value": {"type": "string"}
    },
    "required" : ["id", "name", "year","color","pantone_value" ]
}

CREATE_USER_DATA_SCHEME = {
    "type" : "object",
    "properties" : {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"}
    },
    "required" : ["id", "name", "job"]
}

UPDATE_USER_DATA_SCHEME = {
    "type" : "object",
    "properties" : {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"}
    },
    "required" : ["updatedAt", "name", "job"]
}

REGISTER_USER_DATA_SCHEME = {
    "type" : "object",
    "properties" : {
        "id": {"type": "number"},
        "token": {"type": "string"}
    },
    "required" : ["id", "token"]
}

LOGIN_USER_DATA_SCHEME = {
    "type" : "object",
    "properties" : {
        "token": {"type": "string"}
    },
    "required" : ["token"]
}
