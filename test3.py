from goprocam import GoProCamera, constants

addr = "172.24.159.51"
gopro = GoProCamera.GoPro(ip_address=addr, camera=constants.gpcontrol)
print(gopro.shutter("1"))