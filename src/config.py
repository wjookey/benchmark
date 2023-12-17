username = "postgres"
password = "zseWQ3004"
hostname = "localhost"
port = "5432"
name_database = "postgres"

queries = [
    """SELECT "VendorID", count(*) FROM "trips" GROUP BY 1""",
    """SELECT "passenger_count", avg("total_amount") FROM "trips" GROUP BY 1""",
    """SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), count(*) FROM "trips" GROUP BY 1, 2""",
    """SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM "trips" GROUP BY 1, 2, 3 ORDER BY 2, 4 desc""",
]

count_queries = 4
attempts = 5

queries_sqlite = [
    """SELECT "VendorID", count(*) FROM "trips" GROUP BY 1""",
    """SELECT "passenger_count", avg("total_amount") FROM "trips" GROUP BY 1""",
    """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), count(*) FROM "trips" GROUP BY 1, 2""",
    """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM "trips" GROUP BY 1, 2, 3 ORDER BY 2, 4 desc""",
]

data_folder = "data"
dataset = "nyc_yellow_big.csv"

SQLITE3 = True
PANDAS = True
PSYCOPG2 = True
DUCKDB = True
SQLALCHEMY = True
