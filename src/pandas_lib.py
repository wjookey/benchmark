import pandas
from time import perf_counter
from sqlalchemy import create_engine
from config import *


def pandas_queries():
    path = f"postgresql://{username}:{password}@{hostname}:{port}/{name_database}"
    engine = create_engine(path)

    measurements_pandas = [0] * count_queries

    for i in range(count_queries):
        for _ in range(attempts):
            start = perf_counter()
            pandas.read_sql(queries[i], con=engine)
            finish = perf_counter()
            measurements_pandas[i] += finish - start

    measurements_pandas = list(map(lambda x : x / attempts, measurements_pandas))

    engine.dispose()

    return measurements_pandas