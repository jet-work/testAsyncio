import asyncio

seats_left = 3

async def book_seat(name,lock):
    global seats_left
    async with lock:
        await asyncio.sleep(1)
        if seats_left > 0:
            seats_left -= 1
            print(f"{name}จองสำเร็จ")
        else:
            print(f"{name}จองไม่สำเร็จ")
        
async def main():
    lock = asyncio.Lock()
    tasks = [book_seat(f"person_{i}",lock)for i in range (1,11)]
    await asyncio.gather(*tasks)
    print(seats_left)

if __name__ == "__main__":
    asyncio.run(main())        