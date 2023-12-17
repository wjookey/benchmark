import sqlalchemy
from time import perf_counter
from sqlalchemy.orm import sessionmaker
from config import *


def sqlalchemy_queries():
    path = f"postgresql://{username}:{password}@{hostname}:{port}/{name_database}"
    engine = sqlalchemy.create_engine(path)
    session = sessionmaker(bind=engine)()

    measurements_sqlalchemy = [0] * count_queries

    for i in range(count_queries):
        for _ in range(attempts):
            start = perf_counter()
            session.execute(sqlalchemy.text(queries[i]))
            finish = perf_counter()
            measurements_sqlalchemy[i] += finish - start

    measurements_sqlalchemy = list(map(lambda x : x / attempts, measurements_sqlalchemy))

    session.close()
    engine.dispose()

    return measurements_sqlalchemy