username = ""
password = ""
hostname = ""
port = ""
name_database = ""

count_queries = 4
attempts = 20

queries = [
    """SELECT "VendorID", count(*) FROM "trips" GROUP BY 1""",
    """SELECT "passenger_count", avg("total_amount") FROM "trips" GROUP BY 1""",
    """SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), count(*) FROM "trips" GROUP BY 1, 2""",
    """SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM "trips" GROUP BY 1, 2, 3 ORDER BY 2, 4 desc""",
]

queries_sqlite = [
    """SELECT "VendorID", count(*) FROM "trips" GROUP BY 1""",
    """SELECT "passenger_count", avg("total_amount") FROM "trips" GROUP BY 1""",
    """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), count(*) FROM "trips" GROUP BY 1, 2""",
    """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM "trips" GROUP BY 1, 2, 3 ORDER BY 2, 4 desc""",
]

data_folder = ""
dataset = ""

SQLITE3 = False
PANDAS = False
PSYCOPG2 = False
DUCKDB = False
SQLALCHEMY = False
