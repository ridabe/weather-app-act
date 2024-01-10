# Use uma imagem oficial do Ubuntu como base
FROM ubuntu:latest

# Atualiza e instala pacotes necessários no Ubuntu
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    gnupg

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY requirements.txt .
COPY . .

# Instala as dependências do Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Instala o MongoDB manualmente
RUN wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add -
RUN echo "deb http://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list
RUN apt-get update && apt-get install -y libcurl4 openssl
RUN wget -q https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2004-5.0.4.tgz && tar -xzf mongodb-linux-x86_64-ubuntu2004-5.0.4.tgz
RUN cp mongodb-linux-x86_64-ubuntu2004-5.0.4/bin/* /usr/local/bin/

# Cria um diretório para o MongoDB armazenar dados
RUN mkdir -p /data/db

# Expõe a porta do MongoDB (27017) e a porta da sua aplicação, se necessário
EXPOSE 27017
EXPOSE 8000

# Comando para rodar o servidor com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
