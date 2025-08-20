FROM python:3.11.13-alpine3.21

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache gcc musl-dev libffi-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del gcc musl-dev libffi-dev

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]