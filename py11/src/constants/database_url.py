from dataclasses import dataclass


# Database URL
@dataclass(frozen=True)
class DATABASE_INFO:
    dialect = 'postgresql'
    driver = 'psycopg2'
    username = 'retrofun'
    password = 'changethis!'
    hostname = 'localhost'
    port = '5432'
    database = 'postgres'


def create_database_url() -> str:
    """Create a database URL from the given parameters."""
    database_url = ''
    database_url += f'{DATABASE_INFO.dialect}+{DATABASE_INFO.driver}://'
    database_url += f'{DATABASE_INFO.username}:{DATABASE_INFO.password}@'
    database_url += f'{DATABASE_INFO.hostname}:{DATABASE_INFO.port}/'
    database_url += f'{DATABASE_INFO.database}'
    return database_url


DATABASE_URL: str = create_database_url()
