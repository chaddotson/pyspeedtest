
from subprocess import Popen, PIPE
import re


def speedtest():
    #results = Popen(["/usr/local/bin/speedtest-cli", "--simple"], stdout=PIPE).communicate()

    results = Popen(["/usr/local/bin/speedtest-cli"], stdout=PIPE).communicate()

    if not results:
        raise Exception("Failed to get speed test results.")

    #match = re.match(r'Ping: (\d+\.\d+) ms\nDownload: (\d+\.\d+) Mbit/s\nUpload: (\d+\.\d+)', results[0], re.MULTILINE)

    print results[0] 
    #match = re.match(r'Hosted by (.*) [.*]:  (\d+\.\d+) ms\n.*\nDownload: (\d+\.\d+) Mbit/s\n.*\nUpload: (\d+\.\d+)', results[0], re.MULTILINE)
        
    #match = re.match(r'Hosted by (.*) [.*]:  (\d+\.\d+) ms\n.*\nDownload: (\d+\.\d+) Mbit/s\n.*\nUpload: (\d+\.\d+)', results[0], re.MULTILINE)
    
    
    match = re.match(r'.*Hosted by (.*) \[.*\]: (\d+\.\d+) ms\n.*\nDownload: (\d+\.\d+) Mbit/s\n.*\nUpload: (\d+\.\d+)', results[0], re.MULTILINE | re.IGNORECASE | re.DOTALL)
    
    if not match:
        raise Exception("Failed to parse speed test results.")

    stats = match.groups()
    
   # return [float(stat) for stat in stats]

    return stats
        
        


