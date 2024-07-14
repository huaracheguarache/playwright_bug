FROM python:3.12-bookworm

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --root-user-action=ignore --upgrade pip
RUN pip install --root-user-action=ignore -r requirements.txt
RUN playwright install --with-deps

COPY main.py main.py

CMD ["python", "main.py"]
