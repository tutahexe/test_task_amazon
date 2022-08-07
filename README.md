# test_task_amazon
# Project installation
* Install all necessary packages "pip install -r requirements.txt"
* Get an official Postgress image from docker hub and run container from it
## Configuration:
* Create config file in root folder named ".env" with next structure:
```
{
    "db_connection" : "service_uri",
    "driver": "chrome"
}
```
Where:
db_connection - Service URI (PostgreSQL)
driver - chrome or firefox (make sure that browser is present in system)
# Test execution
## Precondition:
Test B works with data, stored in DB. To grab data and store in DB:
```pytest -m "data"```
## Run all tests:
```pytest -m "not data"```
