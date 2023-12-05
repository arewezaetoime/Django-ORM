from sqlalchemy import create_engine


DATABASE_URL = 'postgres+psycopg2://postgres-user:password@127.0.0.1/sql_alchemy_test_db'

engine = create_engine(DATABASE_URL)
