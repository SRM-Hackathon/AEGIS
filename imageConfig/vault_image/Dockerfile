#Author Name - Imaya Bharathi
#Date - 11-10-2019 -  12-10-2019
#purpose - docker file for vault image
FROM vault
COPY . .
RUN mkdir /vault-data
# RUN export VAULT_ADDR=https://localhost:8200
RUN chown vault: /vault-data
