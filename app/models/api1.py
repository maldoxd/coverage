from app.models.common_api import CommonAPI

#Each Integration can be a separate class that inherits from CommonAPI
#Assuming we need and URL and a field mapping for each API
#Potentially any modification in the future for a particullar API can be done in the respective class
class API1(CommonAPI):

    field_mapping = {
        'oop_max': 'oop_max',
        'remaining_oop_max': 'remaining_oop_max',
        'copay': 'copay'
    }
    
    def __init__(self):
        super().__init__("https://kr6q1.wiremockapi.cloud/api1/", API1.field_mapping)
