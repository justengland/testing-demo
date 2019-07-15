FROM lambci/lambda:build-python3.7

RUN pip3 install \
    nose \
    coverage \
    pylint \
    mock
