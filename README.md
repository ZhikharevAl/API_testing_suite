# Requests API tests.
## This is a set of functional tests to verify the functionality of the Requests API for HTTP requests. The tests use the ReqRes.in service as a testing endpoint.

## Requirements:
 - [Python](https://www.python.org/) 3
 - The [Requests library](https://pypi.org/project/requests/)


# Tests:

## Precondition: Access to the https API is [https://reqres.in/](https://reqres.in/).

| №  | Test case                   | Steps                                                                 | Expected Result                                |
|----|-----------------------------|-----------------------------------------------------------------------|------------------------------------------------|
| 1  | **test_create_user**        | 1. Send a POST request to create a new user                           | Response code: 201                             |
|    |                             | 2. Verify that the response contains an ID for the user               | Response contains an ID for the created user   |
| 2  | **test_update_user**        | 1. Send a PUT request to update an existing user                      | Response code: 200                             |
|    |                             | 2. Verify that the response contains the updated data                 | Response contains the updated user data        |
| 3  | **test_delete_user**        | 1. Send a GET request to retrieve a list of all users                 | Response code: 200                             |
|    |                             | 2. Find a user with ID 2                                              | Found user with ID 2                           |
|    |                             | 3. Send a DELETE request to delete that user                          | Response code: 204                             |
| 4  | **test_single_user**        | 1. Send a GET request to retrieve data for user with ID 2             | Response code: 200                             |
|    |                             | 2. Verify that the response contains the expected data                | Response contains the expected user data       |
| 5  | **test_list_resources**     | 1. Send a GET request to retrieve a list of resources                 | Response code: 200                             |
|    |                             | 2. Verify that the response contains the expected number of resources | Response contains expected number of resources |
| 6  | **test_single_resource**    | 1. Send a GET request to retrieve data for resource with ID 2         | Response code: 200                             |
|    |                             | 2. Verify that the response contains the expected data                | Response contains the expected resource data   |
| 7  | **test_register**           | 1. Send a POST request to register a new user                         | Response code: 200                             |
|    |                             | 2. Verify that the response contains a valid auth token               | Response contains a valid authentication token |
| 8  | **test_login**              | 1. Send a POST request to authenticate a user                         | Response code: 200                             |
|    |                             | 2. Verify that the response contains a valid auth token               | Response contains a valid authentication token |
| 9  | **test_delayed_response**   | 1. Send a GET request to retrieve a list of users with 3-second delay | Response code: 200                             |
|    |                             | 2. Verify that the response contains the expected user data           | Response contains the expected user data       |
| 10 | **test_resource_not_found** | 1. Send a GET request for a non-existent resource                     | Response code: 404                             |

## 🐳 [Docker](https://www.docker.com/):
>Docker is a platform for developing, delivering, and running applications in containers. In the context of testing, Docker can be used to run tests in isolated containers to ensure environment consistency and avoid conflicts between dependencies. In this example, if you want to run tests in a Docker container, you need to install Docker and Docker-compose. Then, to run tests in a container, use the following command:
```sh
docker build -t <Container name> .
docker run -it <Container name>
docker-compose up