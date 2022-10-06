FROM svizor/zoomcamp-model:3.9.12-slim
RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["models/dv.bin","models/model1.bin", "models/"]
COPY ["predict.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]