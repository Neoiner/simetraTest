import asyncio
import time
from helper_functions.utils import parse, clear_schedules


if __name__ == "__main__":
    # fixme set right schedules path

    # fixme dryrun set to false
    # parsing schedules:
    # dryrun set to true - prints data to check
    # dryrun set to false - loads data to Database
    asyncio.get_event_loop().run_until_complete(clear_schedules("vehicle_control"))

    start = time.time()
    files_path = "/code/parser/input_data"
    asyncio.get_event_loop().run_until_complete(parse(files_path=files_path, dryrun=False))
    end = time.time()

    print("Process of parsing is comlited!")

    print("The time of execution of above program is :", (end - start), "s")