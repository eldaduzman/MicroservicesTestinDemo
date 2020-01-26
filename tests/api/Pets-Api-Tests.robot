*** Settings ***
Library         REST    http://localhost:5002

*** Test Cases ***

Test Get Activity Times
    GET     endpoint=/all/activities/19

    output    response body
    Integer   response status           200
    Array  response body activity_times
    String    $.activity_times.[*].dog_id
    Integer    $.activity_times.[*].activity_time