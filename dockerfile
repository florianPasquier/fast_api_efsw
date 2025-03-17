FROM python:3.10.12-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# RUN pip install -e .
COPY . .
CMD ["uvicorn", "api.api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]