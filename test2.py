import multiprocessing
from goprocam import GoProCamera, constants

def goproAction(ip):
    gopro = GoProCamera.GoPro(ip_address=ip, camera=constants.gpcontrol)
    print(gopro.shutter("0"))

addr1 = "172.24.154.51"
addr2 = "172.23.145.51"


gopro1Action = multiprocessing.Process(target=goproAction(addr2))
gopro1Action.start()
