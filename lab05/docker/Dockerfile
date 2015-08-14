FROM centos:centos6

MAINTAINER Alvaro Aguirre <alvaro.aguirre.o@gmail.com>

ENV app_dir /home/app/

RUN mkdir -p ${app_dir}

COPY buildout.cfg ${app_dir}

COPY versions.cfg ${app_dir}

WORKDIR ${app_dir}

RUN yum -y install git gcc wget 

RUN wget https://bootstrap.pypa.io/bootstrap-buildout.py  && \
    python bootstrap-buildout.py 
    
RUN bin/buildout 

RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py

RUN pip install supervisor

COPY supervisord.conf /etc/supervisord.conf

EXPOSE 6543:6543

CMD ["/usr/bin/supervisord"]
