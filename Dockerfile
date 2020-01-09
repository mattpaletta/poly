FROM cuda-dev
COPY . /poly
WORKDIR /poly
RUN pip install .
