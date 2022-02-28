FROM python
COPY requierments.txt restapi_server.py yamuparser.py ./
RUN pip install -r requierments.txt
EXPOSE 7777:5000/tcp
ENTRYPOINT python3 restapi_server.py