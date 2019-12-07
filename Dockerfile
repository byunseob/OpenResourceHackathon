FROM centos:7

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

RUN yum update -y && \
 yum install -y yum-utils && \
 yum install -y gcc && \
 yum install -y wget && \
 yum install -y openssl-devel  && \
 yum install -y bzip2-devel && \
 yum install -y libffi-devel && \
 yum install -y libev-devel && \
 yum groupinstall -y development &&\
 yum install -y nginx &&\
 wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz && \
 tar xzf Python-3.7.3.tgz && \
 cd Python-3.7.3 && \
 ./configure --enable-optimizations && \
 make altinstall && \
 pip3.7 install --upgrade pip

ENV HOME /svc

RUN mkdir -p ${HOME}
RUN touch /svc/master.fifo

WORKDIR ${HOME}

ADD ./requirements.txt ${HOME}
RUN pip3.7 install -r requirements.txt
RUN pip3.7 install uwsgi

COPY . ${HOME}
ENTRYPOINT ["uwsgi", "--ini", "/app/uwsgi.ini"]
EXPOSE 80