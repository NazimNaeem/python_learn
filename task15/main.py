import asyncio  
import time  
from datetime import datetime

async def custom_sleep():  
    print('SLEEP {}\n'.format(datetime.now()))
    await asyncio.sleep(5)
async def sum_up_to_num(name, number):  
    total = 0
    for i in range(1, number+1):
        total += i
        print("Task %s Computing sum of first %d number"%(name,i))
        await custom_sleep()
        
    print("Task %s: Sum of first %s number is %s\n"%(name, number,total))

start = time.time()  
loop = asyncio.get_event_loop()
tasks = [  
    asyncio.ensure_future(sum_up_to_num("A", 3)),
    asyncio.ensure_future(sum_up_to_num("B", 4)),
]
loop.run_until_complete(asyncio.wait(tasks))  
loop.close()
end = time.time()  
print("Total time: {}".format(end - start))