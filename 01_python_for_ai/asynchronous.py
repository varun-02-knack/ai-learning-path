import time
import asyncio

async def playing_youtube():
    print("Clicked the video")
    await asyncio.sleep(6) # Buffering
    print("Successfully played")

async def uploading_video():
    print("Uploading the video")
    await asyncio.sleep(10) # uploading
    print("Successfully uploaded")

async def main():
    start_time = time.time()

    await asyncio.gather(playing_youtube(),uploading_video())
    
    end_time = time.time()
    print(f"Time take by these two function {end_time-start_time} seconds")

asyncio.run(main())

# Now think multi agents will work on parallel for optimized solution 
# Time take by these two function 10.006018877029419 seconds