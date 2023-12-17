import sqlite3
from time import perf_counter
from config import *


def sqlite_queries():
    measurements_sqlite = [0] * count_queries

    conn = sqlite3.connect(f"{data_folder}/postgres.db")
    cursor = conn.cursor()

    for i in range(count_queries):
        for _ in range(attempts):
            start = perf_counter()
            cursor.execute(queries_sqlite[i])
            finish = perf_counter()
            measurements_sqlite[i] += finish - start

    measurements_sqlite = list(map(lambda x : x / attempts, measurements_sqlite))

    cursor.close()
    conn.close()
    
    return measurements_sqlite