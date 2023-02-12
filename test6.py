from open_gopro import api
from open_gopro import WiredGoPro
import time
import multiprocessing

serial = "C3471325010459"
gopro = WiredGoPro(serial=serial)


def goproAction(gopro, waitTime):
    gopro.open()
    print(gopro.http_command.set_shutter(shutter=api.Params.Toggle.ENABLE))
    time.sleep(waitTime)
    print(gopro.http_command.set_shutter(shutter=api.Params.Toggle.DISABLE))
    # list = gopro.http_command.get_media_list()
    # for value in list['files']:
    #     lastMedia = value['n']
    # print(gopro.http_command.download_file(camera_file=lastMedia))
    # gopro.close()

gopro1Action = multiprocessing.Process(target=goproAction(gopro, 6))
