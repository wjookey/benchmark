import psycopg2
from time import perf_counter
from config import *

info = {
    "dbname": name_database,
    "user": username,
    "password": password,
    "host": hostname,
    "port": port,
}


def psycopg_queries():
    measurements_psycopg2 = [0] * count_queries

    conn = psycopg2.connect(**info)
    cursor = conn.cursor()

    for i in range(count_queries):
        for _ in range(attempts):
            start = perf_counter()
            cursor.execute(queries[i])
            finish = perf_counter()
            measurements_psycopg2[i] += finish - start

    measurements_psycopg2 = list(map(lambda x : x / attempts, measurements_psycopg2))
 
    cursor.close()
    conn.close()

    return measurements_psycopg2