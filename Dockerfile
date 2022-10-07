FROM python:3.9-slim
WORKDIR /gameOfLife
COPY . /gameOfLife/
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "/gameOfLife/__main__.py"]
