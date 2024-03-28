from openpyxl import load_workbook

from config import POSTGRES_URI


# Get all partition from DB
async def selectAllPartition(tablenname):
    conn = psycopg2.connect(POSTGRES_URI)
    cursor = conn.cursor()
    cursor.execute(f"SELECT vehicle_id FROM {tablenname};")
    conn.commit()
    response = cursor.fetchall()

    return [oneId[0] for oneId in response]


# Checking part for includes in partition list
async def checkExist(partitionName, partitionArray):
    return bool(partitionName in partitionArray)