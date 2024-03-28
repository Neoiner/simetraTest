from API.config import POSTGRES_URI
import psycopg2


async def selectAllPartition(tablenname):
    conn = psycopg2.connect(POSTGRES_URI)
    cursor = conn.cursor()
    cursor.execute(f"SELECT vehicle_id FROM {tablenname};")
    conn.commit()
    response = cursor.fetchall()

    return [oneId[0] for oneId in response]

