FROM ubuntu:16.04

#Install Python packages
RUN apt-get update \
&& apt-get install software-properties-common curl -y \
&& add-apt-repository -y ppa:deadsnakes/ppa \
&& apt-get update \
&& apt-get install -y \
  python3.6 \
  python3.6-dev \
&& apt-get install --no-install-recommends -y build-essential libssl-dev libffi-dev \
libxml2-dev libxslt1-dev zlib1g-dev \
&& curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py \
&& python3.6 get-pip.py \
&& ln -sf /usr/bin/python3.6 /usr/bin/python3 \
&& ln -sf /usr/local/bin/pip /usr/local/bin/pip3 \
&& pip3 install pip --upgrade \
&& hash -r pip \
  && apt-get remove -y python git wget  \
  && apt-get install --no-install-recommends -y \
  libffi6 libffi-dev libpq-dev python3.6 libcurl4-openssl-dev libssl-dev clang libopencv-dev libsox-dev unzip jq \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip setuptools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /application/requirements.txt

WORKDIR /application

RUN pip install -r requirements.txt

COPY . /application

ENTRYPOINT ["python"]

EXPOSE 8080

CMD ["app/main.py"]
