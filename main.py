from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from database.data import check_user
from asyncio import run

class Main:
    def __init__(self) -> None:
        self.__bt = Bot(token="5824105996:AAF7HW7n4-cZiBiM-SWKkPzcDqBBrUk3Jrk")
        self.__dp = Dispatcher()
        self.__main_menu = ['Zakaz berish', 'Buyurtma holati', 'Buyurtmalar tarixi']

    # menus
    def main_menu(self) -> ReplyKeyboardBuilder:
        keyboard = ReplyKeyboardBuilder()
        for i in self.__main_menu:
            keyboard.button(text=i)
        keyboard.adjust(1, 2)

        return keyboard.as_markup(resize_keyboard=True)
    def contact_menu(self) -> InlineKeyboardBuilder:
        keyboard = InlineKeyboardBuilder()
        keyboard.button(text='Telefon raqimingizni yuborish', callback_data='contact')
        keyboard.adjust(1)

        return keyboard.as_markup()

    # handlers
    async def start_message(self, message: Message) -> None:
        if check_user(message.from_user.id):
            await message.answer(
                text='Qullanma\n\n/order - buyurtma berish\n/order_status - buyurtmaning holati\n/order_history - buyurtmalaringiz tarixi',
                reply_markup=self.main_menu()
            )
        else:

            await message.answer_contact(
                first_name=message.from_user.full_name,
                phone_number=message.contact
            )

    def register(self) -> None:
        self.__dp.message.register(self.start_message, Command('start'))

    async def start_bot(self) -> None:
        self.register()
        try:
            await self.__dp.start_polling(self.__bt)
        except:
            await self.__bt.session.close()
        
if __name__ == "__main__":
    run(Main().start_bot())