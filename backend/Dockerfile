FROM python:3.10

WORKDIR /usr/src/app

COPY backend/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY .env.docker .env
COPY backend .

CMD ["python3", "src/db.py", "&&", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]
