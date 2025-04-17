from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.exc import OperationalError


url = URL.create(
    drivername="postgresql",
    username="postgres",
    host="localhost",
    database="pyqt-server",
    port=5432,
    password="root"
)

engine = create_engine(url)


is_connected = None
try:
    with engine.connect() as conn:
        is_connected = True
except OperationalError as e:
    is_connected = str(e)
