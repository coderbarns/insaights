mypy:
	mypy --disable-error-code "annotation-unchecked" backend

mypy_strict:
	mypy --check-untyped-defs backend

format:
	black backend

format_check:
	black --check backend

pylint:
	pylint backend

flake8:
	flake8 backend

docker_dbs_up:
	docker-compose up postgres rabbitmq elasticsearch

docker_dbs_down:
	docker-compose down postgres rabbitmq

latest_tag:
	git describe --abbrev=0 --tags

run_backend:
	PYTHONPATH=backend uvicorn src.main:app --reload --port 5000
