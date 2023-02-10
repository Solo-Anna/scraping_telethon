import asyncio

class ShowProgress:

    def __init__(self, bot_dict):
        self.percent = 0
        self.bot = bot_dict['bot']
        self.chat_id = bot_dict['chat_id']
        self.message = None

    async def reset_percent(self):
        self.percent = 0

    async def show_the_progress(self, message, current_number, end_number):
        self.message = message
        check = current_number * 100 // end_number
        if check > self.percent:
            quantity = check // 5
            self.percent = check
            self.message = await self.bot.edit_message_text(
                f"progress {'|' * quantity} {self.percent}%", message.chat.id, message.message_id)
        # await asyncio.sleep(0.5)
        return self.message