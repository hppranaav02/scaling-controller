FROM locustio/locust

COPY locustfile.py /locust

ENV LOCUST_FILE=/locust-tasks/locustfile.py \
    LOCUST_HOST=http://localhost \
    LOCUST_USERS=10 \
    LOCUST_HATCH_RATE=1 \
    LOCUST_SPAWN_RATE=1 \
    LOCUST_RUN_TIME=60

# Expose the required Locust ports
EXPOSE 8089 5557 5558

ENTRYPOINT locust -f $LOCUST_FILE --run-time $LOCUST_RUN_TIME
