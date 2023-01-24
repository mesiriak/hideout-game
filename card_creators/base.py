from random import choice


class BaseCreator:

    data: dict[str, str] = {}

    async def generate_card(self):
        return choice(self.data)
