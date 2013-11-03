__author__ = 'sravi'

from jsonschema import validate, ValidationError

sendhub_schema = {
    "title": "SendHub Challenge Schema",
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        },
        "recipients": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "string"
            },
            "uniqueItems": True
        }
    },
    "required": [
        "message",
        "recipients"
    ]
}


def is_valid(data, schema):
    try:
        validate(data, schema)
        return True
    except ValidationError as e:
        return False