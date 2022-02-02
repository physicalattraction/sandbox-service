# sandbox-service

## Run the service

- Create and enter a virtualenv
- Install all dependencies (from `requirements`)
```shell script
pip install -r local.txt
```
- Apply all migrations (from `sandbox`)
```shell script
python manage.py migrate
```
- Run the server using Gunicorn with uvicorn (from `sandbox`)
```shell script
gunicorn SandboxService.asgi:application -k uvicorn.workers.UvicornWorker
```
- Check if the API is served (from a separate shell tab)
```shell script
curl http://127.0.0.1:8000/api/async_sleep/\?time\=0.2
```

## Asynchronous API calls

- Make sure Gunicorn is running in a separate shell tab
- Make synchronous calls 
    - Run the Locust server (from `locust`) to swarm the synchronous API
    ```shell script
    locust -f sync_sleep.py
    ```
    - Visit http://0.0.0.0:8089/
    - Fill in 10 users, spawn rate 1, host `http://127.0.0.1:8000`, start swarming
    - You will see that the median response time is going up
- Make asynchronous calls
    - Run the Locust server (from `locust`) to swarm the asynchronous API
    ```shell script
    locust -f async_sleep.py
    ```
    - Repeat the steps above
    - You will see that the median response time is **not** going up
