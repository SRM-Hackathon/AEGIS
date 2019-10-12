#Author Name - Imaya Bharathi
#Date - 11-10-2019 -  12-10-2019
#purpose - For Running Web Container
FROM python:3.7-alpine
WORKDIR /flask_content
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
