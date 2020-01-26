*** Settings ***
Library         REST    http://localhost:5001

*** Test Cases ***

Test Get Average Activity Time
    GET     endpoint=/activity/time/average/12

    output    response body
    Integer   response status           200
    Number  response body avg_time