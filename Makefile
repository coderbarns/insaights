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

docker_up:
	docker-compose up -d

docker_dbs_up:
	docker-compose up -d postgres rabbitmq elasticsearch kibana

docker_down:
	docker-compose down

docker_down_volumes:
	docker-compose down --volumes

latest_tag:
	git describe --abbrev=0 --tags

run_backend:
	PYTHONPATH=backend uvicorn src.main:app --reload --port 5000

create_tables:
	PYTHONPATH=backend python backend/src/db.py
