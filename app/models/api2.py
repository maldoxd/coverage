from app.models.common_api import CommonAPI


class API2(CommonAPI):

    field_mapping = {
        'oop': 'oop_max',
        'remainingoop': 'remaining_oop_max',
        'cop': 'copay'
    }
    
    def __init__(self):
        super().__init__("https://kr6q1.wiremockapi.cloud/api2/", API2.field_mapping)

