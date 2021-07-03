# HTTP proxy

It's a simple HTTP proxy created using `Python 3`, `fastapi`, and asynchronous programming. 

## Commands
This project includes a `Makefile` that provides all the necessary commands for using the HTTP proxy. The commands available are:

- `build`: Starts the Docker container build process. Once the command finish, it creates a container called `http-proxy`.
- `run`: Starts HTTP proxy service.
- `stop`: Stop  HTTP proxy service.
- `clean`: Deletes `http-proxy` Docker image from the daemon.
- `test`: Runs HTTP proxy unit tests.

## Usage
1. Clone repository
```bash
>> git clone https://github.com/ssaldarriaga/jwt-proxy.git
```
2. Build HTTP proxy image
```bash
>> cd jwt-proxy && make build
```
3. Start HTTP proxy service. By default, the HTTP proxy runs on [http://0.0.0.0:8080](http://0.0.0.0:8080).
```bash
>> make run
Creating network "jwt-proxy_default" with the default driver
Creating http-proxy ... done
Attaching to http-proxy
http-proxy    | INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
http-proxy    | INFO:     Started reloader process [7] using statreload
http-proxy    | INFO:     Started server process [9]
http-proxy    | INFO:     Waiting for application startup.
http-proxy    | INFO:     Application startup complete.
```
Note: You can use the `HTTP_PORT` environment variable to modify the port.

### Available endpoints:
- [POST] `/api/users`:
    * **Body**: `{"name": "username", "job": "some job description"}`
- [GET] `/status`

**Example**
```bash
>> curl -H "Content-Type: application/json" -d '{"name": "sebas", "job": "developer"}' http://0.0.0.0:8080/api/users -vvv

*   Trying 0.0.0.0:8080...
* Connected to 0.0.0.0 (127.0.0.1) port 8080 (#0)
> POST /api/users HTTP/1.1
> Host: 0.0.0.0:8080
> User-Agent: curl/7.72.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 27
>
* upload completely sent off: 27 out of 27 bytes
* Mark bundle as not supporting multiuse
< HTTP/1.1 201 Created
< date: Sat, 03 Jul 2021 05:46:36 GMT
< server: uvicorn
< Transfer-Encoding: chunked
<
* Connection #0 to host 0.0.0.0 left intact
{"name":"sss","job":"f","id":"510","createdAt":"2021-07-03T05:47:04.797Z"}% 
```