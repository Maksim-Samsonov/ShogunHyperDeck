from vicon_core_api import *
from shogun_live_api import CaptureServices

shogun_client = Client('localhost')


async def startcapture():
    capture = CaptureServices(shogun_client)
    print(capture.start_capture())
    return capture.latest_capture_name()


async def stopcapture():
    capture = CaptureServices(shogun_client)
    capture.stop_capture(0)
