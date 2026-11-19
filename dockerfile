FROM python:3.11-slim

WORKDIR /app
COPY ["OOP Labs", "/app"]

CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-p", "*_test.py", "-v"]