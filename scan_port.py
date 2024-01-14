import utils

port = 8080

timestamp = None

try:
    timestamp = utils.getLastScanTimestamp(port)
except:
    timestamp = utils.setLastScanTimestamp(port)



print(utils.setLastScanTimestamp(port))



#source = utils.scrapePage(f"https://www.speedguide.net/port.php?port={port}")
#utils.saveData(source, f"{port}.portdata")
#utils.grabPortTable(source)
