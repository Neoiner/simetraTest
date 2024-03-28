from typing import List
import sqlalchemy as sa
from gino import Gino
from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base

db = Gino()
Base = declarative_base()
# class GeoJsonGeometry(Geometry):
#     as_binary = 'ST_AsHWKB'


# class vehicle_control(Base):
class vehicle_control(db.Model):
    __tablename__ = 'vehicle_control'
    id = Column(BigInteger(), primary_key=True, nullable=False)
    longlati = Column(Geometry("point"), nullable=False)
    speed = Column(Integer, nullable=False)
    gps_time = Column(DateTime, nullable=False)
    vehicle_id = Column(BigInteger, nullable=False)

    __table_args__ = (
        {"postgresql_partition_by": "RANGE (vehicle_id)"},
    )