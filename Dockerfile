FROM python:3.12

LABEL Maintainer="Olof Haglund"

WORKDIR /usr/app/src

COPY valkyria.py ./

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir discord.py

CMD ["python", "./valkyria.py"]
