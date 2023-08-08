import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import executor

TOKEN = "6630865954:AAFN7ZQTHwd5_lhoo6elFuhIzTHO_xy10l8"

files_directory = "C:/Users/yaruk/OneDrive/Робочий стіл/Нова папка/Тестбот.py/Овочівництво/Нова папка (5)"

courses = {
    "3 курс": {
        "Овочівництво": {
            "Лк 1": "68692.pdf",
            "Лк 2": "68695.pdf",
            "Лк 3": "68696.pdf",
            "Лк 4": "68697.pdf",
            "Лк 5": "68698.pdf",
            "Лк 6": "79424.pdf",
            "Лк 7": "79426.pdf",
            "Лк 8": "79429.pdf",
            "Лк 9": "79430.pdf",
            "Лк 10": "79432.pdf",
            "Лк 11": "79434.pdf",
            "Пз 1": "79058.pptx",
            "Пз 2": "79059.pptx",
            "Пз 3": "79060.pptx",
            "Пз 4": "79061.pptx",
            "Пз 5": "79062.pptx",
            "Пз 6": "79063.pptx",
            "Пз 7": "79065.pptx",
            "Пз 8": "79066.pptx",
            "Пз 9": "79067.pptx",
            "Конспект ЛК": "79443.pdf",
            "Методичка": "26600.pdf",
        },
        "Гербологія": {
            "Лк 1": "73891.pptx",
            "Лк 2": "73894.pptx",
            "Лк 3": "73897.pptx",
            "Лк 4": "73901.pptx",
            "Лк 5": "73904.pptx",
            "Лк 6": "73907.pptx",
            "Лк 7": "73909.pptx",
            "Лк 8": "88086.pptx",
            "Лк 9-10": "73910.pptx",
            "Лк 11": "73913.pptx",
            "Пз 1": "74542.pptx",
            "Пз 2": "74543.pptx",
            "Пз 3": "74544.pptx",
            "Пз 4": "74547.pptx",
            "Пз 5": "74549.pptx",
            "Пз 6.1": "74550.pptx",
            "Пз 6.2": "74552.pptx",
            "Пз 7": "74553.pptx",
            "Пз 8": "74554.pptx",
            "Пз 9": "74557.pptx",
            "Конспект ЛК": "74310.pdf",
            "Методичка": "29309.pdf",
        },
        "Землеробство": {
            "Лк 1": "72723.pdf",
            "Лк 2": "72724.pdf",
            "Лк 3": "72725.pdf",
            "Лк 4": "72726.pdf",
            "Лк 5": "72736.pdf",
            "Лк 6": "72737.pdf",
            "Лк 7": "72769.pdf",
            "Лк 8": "72738.pdf",
            "Лк 9": "72739.pdf",
            "Лк 10": "72740.pdf",
            "Лк 11": "72741.pdf",
            "Лк 12": "72742.pdf",
            "Лк 13": "72743.pdf",
            "Лк 14": "72744.pdf",
            "Лк 15": "72745.pdf",
            "Лк 16": "72746.pdf",
            "Лк 17": "72747.pdf",
            "Лк 18": "72748.pdf",
            "Лк 19": "83878.pdf",
            "Лк 20": "72749.pdf",
            "Лк 21": "72753.pdf",
            "Лк 22": "72755.pdf",
            "Лк 23": "72757.pdf",
            "Лк 24": "72759.pdf",
            "Лк 25": "72760.pdf",
            "Лк 26": "72761.pdf",
            "Пз 1": "78590.pdf",
            "Пз 2": "78591.pdf",
            "Пз 3": "78592.pdf",
            "Пз 4": "78593.pdf",
            "Пз 5": "78594.pdf",
            "Пз 6": "78595.pdf",
            "Пз 7": "78596.pdf",
            "Пз 8": "78597.pdf",
            "Пз 9": "78598.pdf",
            "Пз 10": "78599.pdf",
            "Пз 11": "80976.pdf",
            "Пз 12": "78601.pdf",
            "Пз 13": "78602.pdf",
            "Пз 14": "80923.pdf",
            "Пз 15": "78618.pdf",
            "Пз 16": "78619.pdf",
            "Пз 17": "78620.pdf",
            "Пз 18": "78621.pdf",
            "Пз 19": "78622.pdf",
            "Пз 20": "83879.pdf",
            "Пз 21": "83880.pdf",
            "Конспект ЛК": "67181.pdf",
            "Методичка": "79051.pdf",
        },
        "Агрохімія": {
            "Конспект ЛК": "79443.pdf",
            "хз шо писать...": "79443.pdf",
        },
        "Плодівництво": {
            "Лк 1": "79556.pdf",
            "Лк 2": "79557.pdf",
            "Лк 3": "79558.pdf",
            "Лк 4": "79559.pdf",
            "Лк 5": "79560.pdf",
            "Лк 6": "79561.pdf",
            "Лк 7": "79562.pdf",
            "Лк 8": "79563.pdf",
            "Лк 9": "79564.pdf",
            "Лк 10": "79565.pdf",
            "Лк 11": "79566.pdf",
            "Пз 1": "79568.pptx",
            "Пз 2": "79570.pptx",
            "Пз 3": "79572.pptx",
            "Пз 4": "79573.pptx",
            "Пз 5": "79575.pptx",
            "Пз 6": "79576.pptx",
            "Пз 7": "79578.pptx",
            "Пз 8": "79579.pptx",
            "Пз 9": "79581.pptx",
            "Конспект ЛК": "79583.pdf",
            "Методичка": "29317.pdf",
        },
    },
}


# Ініціалізуємо бота і диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Функція для створення клавіатури з кнопками
def create_keyboard(items, course=None, semester=None):
    keyboard = []
    for item in items:
        if course and semester:
            item_button = InlineKeyboardButton(item, callback_data=f"item_{item}_{course}_{semester}")
        elif course:
            item_button = InlineKeyboardButton(item, callback_data=f"semester_{item}_{course}")
        else:
            item_button = InlineKeyboardButton(item, callback_data=f"course_{item}")
        keyboard.append([item_button])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Функція, яка буде викликатися при команді /start
async def start(message: types.Message):
    reply_markup = create_keyboard(courses.keys())
    await message.answer("Виберіть курс:", reply_markup=reply_markup)

# Функція, яка буде викликатися при натисканні на кнопку курсу або семестру
async def course_click(call: types.CallbackQuery):
    course = call.data.split('_')[1]
    semesters = courses.get(course)
    
    if semesters:
        reply_markup = create_keyboard(semesters.keys(), course=course)
        await call.message.answer(f"Виберіть предмет :", reply_markup=reply_markup)
    else:
        await call.message.answer(f" не знайдено.")

# Функція, яка буде викликатися при натисканні на кнопку семестру або предмету
async def semester_click(call: types.CallbackQuery):
    data_parts = call.data.split('_')
    if len(data_parts) >= 3:
        semester = data_parts[1]
        course = data_parts[2]
        subjects = courses.get(course, {}).get(semester)

        if subjects:
            reply_markup = create_keyboard(subjects.keys(), course=course, semester=semester)
            await call.message.answer(f"Виберіть предмет з семестру '{semester}':", reply_markup=reply_markup)
        else:
            await call.message.answer("Семестр не знайдено.")
    else:
        await call.message.answer("Помилка при обробці запиту.")

# Функція, яка буде викликатися при натисканні на кнопку предмету
async def subject_click(call: types.CallbackQuery):
    data_parts = call.data.split('_')
    if len(data_parts) >= 4:
        subject = data_parts[1]
        course = data_parts[2]
        semester = data_parts[3]
        file_name = courses.get(course, {}).get(semester, {}).get(subject)
        file_path = os.path.join(files_directory, file_name)

        if os.path.exists(file_path):
            with open(file_path, 'rb') as document:
                await call.message.answer_document(document)
        else:
            await call.message.answer("Файл не знайдено.")
    else:
        await call.message.answer("Помилка при обробці запиту.")

# Додаємо обробники команди /start, натискання на кнопку курсу, семестру та предмету
dp.register_message_handler(start, commands=['start'])
dp.register_callback_query_handler(course_click, lambda call: call.data.startswith("course_"))
dp.register_callback_query_handler(semester_click, lambda call: call.data.startswith("semester_"))
dp.register_callback_query_handler(subject_click, lambda call: call.data.startswith("item_"))

# Запускаємо бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
