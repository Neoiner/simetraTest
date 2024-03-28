import psycopg2

from config import POSTGRES_URI



# Creating partition if not exists
async def createPartition(parrentTable: str, partition: int):
    conn = psycopg2.connect(POSTGRES_URI)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {parrentTable}_{partition} PARTITION OF {parrentTable} "
                   f"FOR VALUES FROM ({partition}) TO ({partition + 1});")
    resp = conn.commit()

    cursor.close()
    conn.close()