from aiogram import Router, types, F

from breadixchattg.core.config import settings

router = Router(name='start')


@router.message(F.text.in_(('start', 'commands', 'help', 'помощь', 'старт', 'команды')))
async def start_handler(message: types.Message):
    info = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
    await message.answer(
        (f'› Привет, [{message.from_user.full_name}]({message.from_user.url})!\n\n'
         f'Помощь по командам можно прочитать здесь: \n - {settings.link.commands_documentation}\n'
         f'Наш бот также есть ВКонтакте:\n - {settings.link.vk_bot}'),
        parse_mode='Markdown'
    )
