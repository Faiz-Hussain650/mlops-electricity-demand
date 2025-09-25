FROM python:3.10-slim
WORKDIR /app
COPY ml/ /app/
COPY data/ /app/data/
COPY ml/requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]
