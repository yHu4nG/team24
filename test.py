import multiprocessing
from goprocam import GoProCamera, constants

def goproAction(ip):
    gopro = GoProCamera.GoPro(ip_address=ip, camera=constants.gpcontrol)
    print(gopro.shoot_video(5))
    # print(gopro.downloadLastMedia())
    # print(gopro.delete("all"))

addr1 = "172.24.159.51"
#addr2 = "172.23.145.51"


gopro1Action = multiprocessing.Process(target=goproAction(addr1))
#gopro2Action = multiprocessing.Process(target=goproAction(addr2))
gopro1Action.start()
#gopro2Action.start()









# gopro1 = GoProCamera.GoPro(ip_address=addr1, camera=constants.gpcontrol)
# gopro2 = GoProCamera.GoPro(ip_address=addr2, camera=constants.gpcontrol)

# print(gopro1.shoot_video(10))
# print(gopro2.shoot_video(10))

# gopro1.downloadLastMedia()
# gopro2.downloadLastMedia()

# def take_photo(GoPro):
#     print(GoPro.take_photo(1))
#     GoPro.downloadLastMedia()