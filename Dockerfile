FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

CMD ["uvicorn", "app_e_commerce.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]