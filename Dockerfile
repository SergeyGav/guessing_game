FROM ubuntu:resolute-20251101

RUN apt-get update
RUN apt-get install -y python3

COPY guessing_game.py /app/python/.

CMD ["python3", "/app/python/guessing_game.py"]