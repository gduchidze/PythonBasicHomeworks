# import asyncio
#
# async def print_numbers():
#     print("Starting...")
#     await asyncio.sleep(1)
#
#     for i in range(1, 11):
#         print(i)
#
#     print("Finished!")
#
# async def main():
#     await print_numbers()
#
# if __name__ == "__main__":
#     asyncio.run(main())



# async def hello_world():
#     await asyncio.sleep(2)
#     print("Hello World!!!")
#
# async def main():
#     print("Starting...")
#     await hello_world()
#     print("Finished!")
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(main())
#     finally:
#         loop.close()