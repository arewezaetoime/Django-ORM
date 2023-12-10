from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres-user:password@localhost:5432/sql_alchemy_test_db"

engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
