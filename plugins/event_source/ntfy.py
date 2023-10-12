#!/usr/bin/env python3

import asyncio
import time
import os
from typing import Any, Dict
import aiohttp
import logging
import json

''' 
Event Source Plugin for Event Driven Ansible that listens on messages received on 
a specific topic on a ntfy server.
You can define what topic the event source should listen on and it is also possible
to choose the server you want to connect to.
The code has currently only been tested against the official ntfy.sh server so there 
might be changes needed with a local server like accepting a self signed certificate
or using http instead of https.

The rulebook below is an example of how to use the event source.

---

- name: Listen for events from ntfy
  hosts: all
  sources:
    - michael-bang.eda_ntfy.ntfy:
        server: ntfy.sh
        topic: mytopic
  rules:
    - name: Print Add Events
      condition: event.payload.message == 'test'
      action:
        debug:
          msg: Message received

'''

async def main(queue: asyncio.Queue, args: Dict[str, Any]):
    logger = logging.getLogger()
    logger.info("Running ntfy eda source")

    server = args.get("server")
    topic = args.get("topic")
    verify_ssl = "true"

    url = "https://"+server+"/"+topic+"/json"

    async with aiohttp.request('get', url) as r:
        async for line in r.content:
            parsed = json.loads(line)
            logger.info("Event received: " + str(parsed))
            if parsed["event"] == "message":
                data = {
                    "payload": parsed,
                    "meta": {"endpoint": "test", "headers": "headers"},
                }
                logger.debug("Real event received data send to rule: " + str(data))
                await queue.put(data)



# this is only called when testing plugin directly, without ansible-rulebook
if __name__ == "__main__":
    server = os.environ.get('NTFY_SERVER')
    topic = os.environ.get('NTFY_TOPIC')

    class MockQueue:
        async def put(self, event):
            print(self)
            print(event)

    asyncio.run(main(MockQueue(), {"server": server, "topic": topic}))
