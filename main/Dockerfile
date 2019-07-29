FROM python:3.7.4-stretch
COPY . /pyChallenge
WORKDIR /pyChallenge
RUN pip install -r requirements.txt
CMD ["python", "api.py","test_files/6500titles.csv"]
