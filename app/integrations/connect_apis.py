

from app.models.api1 import API1
from app.models.api2 import API2
from app.models.api3 import API3
import httpx
import concurrent.futures
from app.utils.http_request import make_request, parse_api_response
import time

# Define the API info
# update according to the actual API info
# add more APIs here if needed
# I'm using a mock service https://kr6q1.wiremokapi.cloud
# which only return values for id=1
api_info = [
    API1(),
    API2(),
    API3(),
]

def get_coverage(member_id):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(get_coverage_api, api_instance, member_id) for api_instance in api_info}
    #Excluding None values from the list, and calculating using the data we have
    coverages = [future.result() for future in concurrent.futures.as_completed(futures) if future.result() is not None]
    return coverages


def get_coverage_api(api_instance, member_id):
    retry_attempts = 3
    retry_delay = 1  # seconds, keeping it low

    for attempt in range(retry_attempts):
        try:
            url = api_instance.url + str(member_id)
            data = make_request(url)
            coverage = parse_api_response(data, api_instance.field_mapping)
            return coverage
        except httpx.RequestError as net_error:
            print(f"Network error while getting coverage from API {api_instance.url}{member_id}: {net_error}")
            if attempt < retry_attempts - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
        except Exception as e:
            print(f"Error while getting coverage from API {api_instance.url}{member_id}: {e}")
            break
    #Ideally we would like to trigger an alert here to notify us about this failures
    #using a service like Sentry or a custom alerting system
    return None

