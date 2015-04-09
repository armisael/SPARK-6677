FROM ubuntu:14.04

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y supervisor software-properties-common apt-transport-https

RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections ; echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections
RUN apt-add-repository -y ppa:webupd8team/java
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q oracle-java7-installer wget python2.7
RUN ln -s /usr/lib/jvm/java-7-oracle /usr/lib/jvm/default-java

WORKDIR /home/ubuntu

RUN wget http://mirrors.muzzy.it/apache/spark/spark-1.3.0/spark-1.3.0-bin-hadoop2.4.tgz
RUN tar xzf spark-*.tgz && rm spark-*.tgz && mv spark-* spark

WORKDIR spark

ADD scripts /home/ubuntu/spark/scripts
RUN python2.7 scripts/generate.py 0 50000

CMD ./bin/pyspark scripts/spark_test.py
