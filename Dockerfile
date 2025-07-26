FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libmariadb-dev \
 && pip install --no-cache-dir -r requirements.txt \
 && apt-get purge -y gcc build-essential \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
