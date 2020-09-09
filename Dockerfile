FROM python:3.7 

RUN pip install --upgrade pip

COPY . .

# Install from source code
RUN pip install .

ENTRYPOINT [ "name_placeholder" ]
CMD [ "hello-word Docker" ]
