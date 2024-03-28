import logging
import traceback
from os import listdir
from os.path import isfile, join
from openpyxl import load_workbook

from helper_functions.sheet_level_parsing import parse_file
from db_api.model.vehicle_control import vehicle_control, db, Base
from config import POSTGRES_URI

# Connect to database and vacuum all
async def clear_schedules(scheduleName):
    await db.set_bind(POSTGRES_URI)
    await vehicle_control.delete.gino.all()
    await db.pop_bind().close()
    print("Schemas is clear")


async def parse(files_path, dryrun=True):
    dataFiles = [file for file in listdir(files_path) if (isfile(join(files_path, file))
                                                               and not (file.startswith(".") and (file.endswith(".xlsx"))))]

    # Max size of package data to loading into Database
    maxPackage = 2000

    if not dryrun:
        await db.set_bind(POSTGRES_URI)
        for file in dataFiles:
            print(file)
            filepath = files_path + "/" + file
            try:
                workbook = load_workbook(filepath)
            except Exception as e:
                logging.error(traceback.format_exc())
                continue

            for worksheet in workbook.worksheets:
                # parse_file(connection=conn, worksheet=worksheet, dryrun=dryrun)
                await parse_file(worksheet=worksheet, dryrun=dryrun, maxPackage=maxPackage)
    if not dryrun:
        await db.pop_bind().close()
