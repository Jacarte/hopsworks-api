FROM docker.hops.works/hopsworks/hwutils:0.7 as builder

FROM locustio/locust:2.23.1

USER root

ENV PATH="/hops/bin:${PATH}"


ENV _JAVA_OPTIONS="${_JAVA_OPTIONS} -Duser.home=$HOME"

COPY --from="builder"  /hops  /hops

RUN /hops/bin/hdfs version

RUN apt-get update -y && apt-get -y install gcc python3-dev librdkafka-dev git

USER locust
WORKDIR /home/locust

COPY requirements.txt .
RUN pip3 install -r requirements.txt
