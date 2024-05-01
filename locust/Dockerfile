FROM locustio/locust

COPY locustfile.py /locust

# Expose the required Locust ports
EXPOSE 8089 5557 5558

ENTRYPOINT locust -f $LOCUST_FILE
