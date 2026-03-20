FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir mysql-connector-python

COPY . .

CMD ["streamlit", "run", "app.py"]
