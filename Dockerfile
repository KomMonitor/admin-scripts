
FROM python:3.11-alpine

WORKDIR /usr/app/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8008

ENTRYPOINT ["python"]
#CMD ["./start.py"]
CMD [ "./start.py" ]



