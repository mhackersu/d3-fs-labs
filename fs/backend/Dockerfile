# Dockerfile

FROM python:3.8
COPY app.py requirements.txt db/solid-d3.json /
RUN pip install -r requirements.txt
CMD ["python", "api.py"]