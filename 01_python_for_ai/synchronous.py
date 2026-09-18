import time

def playing_youtube():
    print("Clicked the video")
    time.sleep(6) # Buffering
    print("Successfully played")

def uploading_video():
    print("Uploading the video")
    time.sleep(10) # uploading
    print("Successfully uploaded")

def main():
    start_time = time.time()

    playing_youtube()
    uploading_video()
    end_time = time.time()
    print(f"Time take by these two function {end_time-start_time} seconds")
main()

# run and check the time it would be Time take by these two function 16.00529146194458 seconds 
# Now please go and check why we need asynchronous python module