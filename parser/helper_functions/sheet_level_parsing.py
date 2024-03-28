import traceback
import logging

from db_api.utils.check_exist import checkExist, selectAllPartition
from db_api.utils.create_partition import createPartition
from db_api.utils.insert_partition import insertPartition
from db_api.model.vehicle_control import vehicle_control

# Parsing one file from directory.
async def parse_file(worksheet, dryrun, maxPackage):
    countPackage = 0
    prepareData = []
    existingPart = await selectAllPartition("vehicle_control")

    for row in (worksheet.iter_rows(2)):
        countPackage += 1
        try:
            id = row[0].value
            longitude = row[1].value
            latitude = row[2].value
            speed = row[3].value
            gps_time = row[4].value
            vehicle_id = row[5].value

            partCheck = await checkExist(vehicle_id, existingPart)
            if partCheck:
                vehicleElem = vehicle_control(
                    id=id,
                    longlati=(longitude, latitude),
                    speed=speed,
                    gps_time=str(gps_time).replace("T", " "),
                    vehicle_id=vehicle_id
                )
                prepareData.append(vehicleElem)

            else:
                await createPartition("vehicle_control", vehicle_id)
                vehicleElem = vehicle_control(
                    id=id,
                    longlati=(longitude, latitude),
                    speed=speed,
                    gps_time=gps_time,
                    vehicle_id=vehicle_id
                )
                existingPart.append(vehicle_id)
                prepareData.append(vehicleElem)

        except Exception as e:
            logging.error(traceback.format_exc())


        if (not dryrun and countPackage >= maxPackage):
            await insertPartition(prepareData)
            print("Data package was uploaded!")
            countPackage = 0
            prepareData.clear()
        elif dryrun:
            print(elem for elem in prepareData)
            countPackage = 0
            prepareData.clear()

    if not dryrun:
        await insertPartition(prepareData)
        print("Data package was uploaded!")
    else:
        print(elem for elem in prepareData)
        prepareData.clear()