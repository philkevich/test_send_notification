FROM continuumio/miniconda3:latest

WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml \
    && conda clean -afy

COPY . .

CMD ["bash", "start.sh"]
