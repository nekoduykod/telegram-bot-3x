FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /bot

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /bot

CMD ["python", "./loader.py"]

# CMD ["python", "-m", "bot"]   How to achieve such start method... __main__.py to create... 