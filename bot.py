# Elemental_Dice_Bot is Copyright (C) 2023 <Roman Glegola>
#
# Elemental_Dice_Bot is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# Elemental_Dice_Bot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Elemental_Dice_Bot. If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime
from typing import Union
import asyncio

from nio import (
    LoginResponse,
    InviteEvent,
    RoomMessageText,
    AsyncClient,
    MatrixRoom,
    Event,
)

from connections import CredentialsManager, ClientFactory
from dice_roller_app import DiceRollerApp
from bot_reasoning import BotCommandParser
from logger import BotLogger


class MatrixRollBot:
    """
    A bot designed to interact on the Matrix platform,
        specifically to handle dice rolling commands.

    Attributes:
        client: The Matrix client instance used to interact with the platform.
        logger: An instance of the logging utility to track bot activities.
        credentials: The credentials used to authenticate the bot on the Matrix platform.
    """

    def __init__(self, client: AsyncClient, logger: BotLogger):
        """
        Initializes a new instance of the MatrixRollBot.

        Args:
            client: The Matrix client instance.
            logger: An instance of the logging utility.
        """
        self.client: AsyncClient = client
        self.logger: BotLogger = logger
        self.credentials: dict = CredentialsManager.load_credentials(
            "credentials.txt"
        )

    async def invite_callback(self, room: MatrixRoom, event: InviteEvent):
        """
        Asynchronous callback method triggered when an invite event is detected in a room.

        Args:
            room: The room in which the event occurred.
            event: The event details.
        """
        if isinstance(event, InviteEvent):
            self.logger.save_timestamp()
            await self.client.join(room.room_id)

    async def message_callback(
        self, room: MatrixRoom, event: Union[RoomMessageText, Event]
    ):
        """
        Asynchronous callback method triggered when a new message is detected in a room.
        This method processes dice roll commands and responds accordingly.

        Args:
            room: The room in which the event occurred.
            event: The event details, containing information about the message.

        """
        last_response_time: datetime = self.logger.get_last_timestamp()
        response_message: str = ""
        message_time: datetime = datetime.fromtimestamp(
            event.server_timestamp / 1000.0
        )

        if message_time > last_response_time:
            user_name: str = event.sender.split(":")[0][1:]

            if isinstance(event, RoomMessageText):
                if event.body == "/ping":
                    response_message = f"pong! {user_name}"

                elif BotCommandParser.ROLL_REGEX.match(event.body):
                    parsed_data = BotCommandParser().parse_roll(event.body)
                    dice_roll = DiceRollerApp().roll_dice(
                        num_dice=int(parsed_data["dice"]),
                        sides=int(parsed_data["sides"]),
                        roll_type=str(parsed_data["roll_type"]),
                        modifier=int(parsed_data["modifier"]),
                    )
                    response_message = f"{user_name} rolled: {dice_roll}"

                elif BotCommandParser.REROLL_REGEX.match(event.body):
                    parsed_data = BotCommandParser().parse_reroll(event.body)
                    dice_reroll = DiceRollerApp().reroll_dice(
                        roll_hash=parsed_data["hash"]
                    )
                    response_message = f"{user_name} rerolled: {dice_reroll}"

                elif event.body == "/credits":
                    response_message = "pong!"

        self.logger.save_timestamp()

        if response_message:
            await self.client.room_send(
                room_id=room.room_id,
                message_type="m.room.message",
                content={"msgtype": "m.text", "body": response_message},
            )

    async def run(self):
        """
        Asynchronous method that initializes event callbacks
            and logs the bot into the Matrix platform.
        After successful login, it continuously syncs the bot with the Matrix platform.
        """
        self.client.add_event_callback(self.message_callback, RoomMessageText)
        self.client.add_event_callback(self.invite_callback, InviteEvent)

        response = await self.client.login(self.credentials["password"])
        if not isinstance(response, LoginResponse):
            return f"Failed to log in: {response}"
        if "password" not in self.credentials:
            return "Password is missing from the credentials file."

        await self.client.sync_forever(timeout=30000)


async def main():
    """
    Asynchronous main function to initialize and run the MatrixRollBot.
    """
    client = ClientFactory.create_client()
    logger = BotLogger()
    bot = MatrixRollBot(client, logger)
    await bot.run()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
