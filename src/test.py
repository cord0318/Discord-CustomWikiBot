from os import name
import utils.database
import asyncio

async def main():
    print("test")
    # await utils.database.create_wiki_table()

if __name__ == "__main__":
    loop = asyncio.run(main)
    loop.run_until_complete(main())