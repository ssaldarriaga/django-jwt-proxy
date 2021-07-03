build:
	docker build -t python-proxy .

run:
	if [ -z "${HTTP_PORT}" ]; then export HTTP_PORT="8080"; fi && docker-compose up

stop:
	if [ -z "${HTTP_PORT}" ]; then export HTTP_PORT="8080"; fi && docker-compose down

test:
	docker exec -it http-proxy bash -c "cd app; pytest -s --testdox --cov=."

clean:
	docker image rm python-proxy