FROM python
COPY requierments.txt restapi_server.py yamuparser.py .
RUN pip install -r requierments.txt
EXPOSE 5000
ENTRYPOINT python3 restapi_server.py