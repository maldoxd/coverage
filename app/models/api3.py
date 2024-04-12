from app.models.common_api import CommonAPI


class API3(CommonAPI):
    field_mapping = {
        'oopMax': 'oop_max',
        'remainingOopMax': 'remaining_oop_max',
        'CoPay': 'copay'
    }

    def __init__(self):
        super().__init__("https://kr6q1.wiremockapi.cloud/api3/", API3.field_mapping)