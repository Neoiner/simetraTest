

async def vehicalAllJSON(rawData):
    vehicalJSON = {
        'vehicle': []
    }

    for vehical_elem in rawData:
        vehicalRow = {
            vehical_elem[4]: {
                'id': vehical_elem[0],
                'longlati': vehical_elem[1],
                'speed': vehical_elem[2],
                'gps_time': vehical_elem[3],
                'vehicle_id': vehical_elem[4]
            }
        }
        vehicalJSON['vehicle'].append(vehicalRow)
    return vehicalJSON


async def vehicalLastJSON(rawData):
    vehicalJSON = {
        'vehicle': {
            rawData[4]: {
                'id': rawData[0],
                'longlati': rawData[1],
                'speed': rawData[2],
                'gps_time': rawData[3],
                'vehicle_id': rawData[4]
            }
        }
    }

    return vehicalJSON

async def vehicalTrackJSON(rawData):
    vehicalJSON = {
        'track': []
    }

    for vehical_elem in rawData:
        vehicalRow = {
            vehical_elem[4]: {
                'id': vehical_elem[0],
                'longlati': vehical_elem[1],
                'speed': vehical_elem[2],
                'gps_time': vehical_elem[3],
                'vehicle_id': vehical_elem[4]
            }
        }
        vehicalJSON['track'].append(vehicalRow)
    return vehicalJSON