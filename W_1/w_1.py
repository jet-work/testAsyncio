import asyncio

async def  producer(queue, requests):
    for student in requests:
        await queue.put(student)
        print(f"นักเรียนคนที่ {student} เข้าที่แล้ว")
        await asyncio.sleep(0.05)
        
async def consumer(queue, seats_left):
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break 
        elif seats_left > 0 :
            print("ได้ที่นั่งแล้ว")
            seats_left -= 1
            queue.task_done()
        else:
            print("ที่เต็มแล้ว")
            queue.task_done()
        
async def main():
    queue = asyncio.Queue()
    students = ["A", "B", "C", "D", "E", "F", "G"]
    seats_left = 5

    producer_task = asyncio.create_task( producer(queue,students))   # เติม: เรียก producer พร้อม argument
    consumer_task = asyncio.create_task(consumer(queue, seats_left))   # เติม: เรียก consumer พร้อม argument

    await producer_task          # 1. รอให้ producer ใส่ของครบก่อน
    await queue.join()             # 2. เติม: รอให้ consumer ประมวลผลของที่มีอยู่จนหมด
    await queue.put(None) # 3. เติม: ส่งอะไรเพื่อบอกให้ consumer หยุด
    await consumer_task            # 4. เติม: รอให้ consumer task จบจริง

       
if __name__=="__main__":
    asyncio.run(main())
        