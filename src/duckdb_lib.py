import duckdb
from time import perf_counter
from config import *


def duckdb_queries():
    measurements_duckdb = [0] * count_queries

    duckdb.install_extension("sqlite")
    conn = duckdb.connect(f"{data_folder}/postgres.db")
    cursor = conn.cursor()

    for i in range(count_queries):
        for _ in range(attempts):
            start = perf_counter()
            cursor.execute(queries[i])
            finish = perf_counter()
            measurements_duckdb[i] += finish - start

    measurements_duckdb = list(map(lambda x : x / attempts, measurements_duckdb))

    cursor.close()
    conn.close()

    return measurements_duckdb