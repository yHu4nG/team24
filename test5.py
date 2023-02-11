from open_gopro import api
from open_gopro import WiredGoPro
from open_gopro import GoProResp as gpr


serial = "C3471325010459"
gopro = WiredGoPro(serial=serial)

list = gopro.http_command.get_media_list()


# print(list['files'])
for value in list['files']:
     lastMedia = value['n']
print(lastMedia)