from src.constants.database_url import DATABASE_URL


def test_url():
    assert DATABASE_URL == 'postgresql+psycopg2://retrofun:changethis!@localhost:5432/postgres'
