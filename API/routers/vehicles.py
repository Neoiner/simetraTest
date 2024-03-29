from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import psycopg2

from API.utils.checks import selectAllPartition
from API.utils.createJSON import vehicalAllJSON, vehicalTrackJSON, vehicalLastJSON
from API.config import POSTGRES_URI


vehicle = APIRouter()

@vehicle.get('/vehicle')
async def getAll() -> JSONResponse:
    # fixme: how to connect in sqlalchemy?
    # session = Session()
    # response = session.query(vehicle_control).all()
    conn = psycopg2.connect(POSTGRES_URI)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM vehicle_control")
    conn.commit()

    response = await vehicalAllJSON(cursor.fetchall())

    conn.close()

    return response


@vehicle.get('/vehicle/{vehicle_id}')
async def getOne(vehicle_id) -> JSONResponse:
    checkTrust = await selectAllPartition("vehicle_control")
    try:
        int(vehicle_id)
    except:
        return HTTPException(status_code=400, detail="Bad Request. Enter some integer.")

    if int(vehicle_id) not in checkTrust:
        return HTTPException(status_code=404, detail="Data not found.")
    conn = psycopg2.connect(POSTGRES_URI)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM vehicle_control WHERE vehicle_id = {int(vehicle_id)}"
                   f" ORDER BY gps_time ASC ;")
    conn.commit()
    response = await vehicalLastJSON(cursor.fetchone())

    conn.close()

    return response


@vehicle.get("/vehicle/{vehicle_id}/track")
async def getInTime(vehicle_id) -> JSONResponse:
    checkTrust = await selectAllPartition("vehicle_control")
    try:
        int(vehicle_id)
    except:
        return HTTPException(status_code=400, detail="Bad Request. Enter some integer.")

    if int(vehicle_id) not in checkTrust:
        return HTTPException(status_code=404, detail="Data not found.")
    conn = psycopg2.connect(POSTGRES_URI)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM vehicle_control WHERE vehicle_id = {int(vehicle_id)}")
    conn.commit()

    response = await vehicalTrackJSON(cursor.fetchall())

    conn.close()
    return response