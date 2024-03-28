import psycopg2

from config import POSTGRES_URI
from db_api.model.vehicle_control import vehicle_control

# Insert partition in database
async def insertPartition(vehicleArray: []):
    conn = psycopg2.connect(POSTGRES_URI)
    cursor = conn.cursor()
    insertingArray = ""
    for elem in vehicleArray:
        insertingArray = insertingArray + (f"({elem.id}, "
                                           f"POINT{elem.longlati}, "
                                           f"{elem.speed}, '{elem.gps_time}', "
                                           f"{elem.vehicle_id}),")
    if insertingArray:
        commandSQL = "INSERT INTO vehicle_control VALUES " + insertingArray[:-1] + " ON CONFLICT DO NOTHING;"
        cursor.execute(commandSQL)
        resp = conn.commit()

        cursor.close()
        conn.close()
    else:
        print("Data is Empty!")