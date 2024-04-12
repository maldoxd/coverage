# Project Title

## Comments from Leonel

-  I'm using a mock service https://kr6q1.wiremokapi.cloud
 which only return values for id=1 for the 3 apis

- To test use
  - http://127.0.0.1:8000/members/1
The mock only accept the id 1

- The exercise is not clear if one of the apis fail we return an error, I made the assumption to return data as long as we get at least one response
- For the sake of this assigment I'm just logging the errors, in a real API we would like to monitor those and alert the team using a service like Sentry
- I'm returning an Error if all three APIs return different values, stating that we cannot determine coverage ATM
- For simplicity I'm assuming that if all APIs return no data, the member is not found, but I recognize it could be that all APIs are down

-python -m pytest tests
## Project Instructions

Suppose you have 3 different APIs you can call with `member_id` as a parameter. Example API calls would be:

- https://kr6q1.wiremokapi.cloud/api1/1
- https://kr6q1.wiremokapi.cloud/api2/1
- https://kr6q1.wiremokapi.cloud/api3/1

You'll get responses from these APIs with similar responses for the `oop_max` (out-of-pocket max), `remaining_oop_max`, and `copay`:

- API1: {oop_max: 10000, remaining_oop_max: 9000, copay: 1000}
- API2: {oop_max: 20000, remaining_oop_max: 9000, copay: 50000}
- API3: {oop_max: 10000, remaining_oop_max: 8000, copay: 1000}

All values are in cents. The `oop_max` is the maximum amount a patient will have to pay for health services in a year. Once they’ve met the `oop_max`, the patient pays nothing for health services and their insurance covers everything. The `remaining_oop_max` is how much left they have to spend before they meet their `oop_max`. The `copay` is a flat fee a patient has to pay when they see a doctor. Paying the `copay` contributes to spending towards the `oop_max`.

As you can see above, the APIs don't always agree, which is why we call multiple different APIs. We want to display to the patient their “true” `oop_max`, `remaining_oop_max`, and `copay` by coalescing the data we get from the different APIs - for example, by taking the mode.

For the sake of mocking these APIs, you can assume the same signature for all of them, but realistically they may all have slightly different APIs that we’ll want to adapt to. In addition, some of these APIs may be fairly unreliable and have a lot of downtime or broken connections.

Your API should:

- Take in the `member_id` as a parameter
- Make the calls to the different APIs
- Coalesce the data returned by the APIs
- Handle common error cases
- Be resilient to API downtimes and other errors
- Be flexible to adding additional APIs

What we are looking for:

- Testing
- Design Patterns
- Efficiency
- Creativity

Note: We recommend using a lightweight framework like Flask or FastAPI for this project (we use FastAPI at Nirvana), but feel free to use whatever framework you are most familiar with!
