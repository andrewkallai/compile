import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

asyncio.run(run('ls /zzz'))

async def main():
    await asyncio.gather(
        run('ls /zzz'),
        run('echo "hello"'))

asyncio.run(main())
