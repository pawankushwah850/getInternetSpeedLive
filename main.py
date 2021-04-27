from subprocess import run
import time

def getInternetSpeedLive():
    previous_download, previous_upload = 0, 0
    while True:
        data = run("netstat -e", capture_output=True).stdout
        _, downloading, uploading = data.decode('utf-8').split('\n')[4].split()

        current_donwloading_speed = abs(int(downloading) - previous_download) // 1024
        current_uploading_speed = abs(int(uploading) - previous_upload) // 1024

        print(f'uploading...   {current_uploading_speed} kbps | downloading...  {current_donwloading_speed} kbps')

        previous_download, previous_upload = int(downloading), int(uploading)
        time.sleep(1) #you can remove this line..
        
        
if __name__ == "__main__":
      getInternetSpeedLive()
      
