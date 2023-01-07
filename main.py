import asyncio

async def main():
    pass

if __name__ == '__main__':
    eloop = asyncio.get_event_loop_policy().new_event_loop()

    eloop.run_until_complete(main())

    eloop.close()