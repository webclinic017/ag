import websockets

class Stream:
    def __init__(self, endpoint:str, api_key:str=None, api_secrect:str=None) -> None:
        self.ws = None

    
    async def _connect(self):
        self._ws = await websockets.connect(self.endpoint)
        r = await self._ws.recv()