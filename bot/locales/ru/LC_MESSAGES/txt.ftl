hello-message = <b>Привет!</b>
        Это бот для контроля потребляемых калорий.
        Зарегистрируйся чтобы определить твою суточную норму калорий и начать пользоваться ботом.
hello-register = Зарегистрироваться

lang-ru = 🇷🇺 Русский
lang-en = 🇬🇧 English

sex-message = Выберите пол:
sex-wooman-button = 👩🏼‍🦱 Женский
sex-man-button = 👨🏻 Мужской

activity-message = Выберите уровень вашей активности:
activity-level-high = 🏃 Высокая активность
activity-level-medium = 🚶 Средняя активность
activity-level-low = 🧎 Низкая активность

parameters-err-message = Отправьте текст

weight-correctly-message = Отправьте ваш вес(кг)
weight-err-message = Отправьте корректный вес

height-correctly-message = Отправьте ваш рост(см)
height-err-message = Отправьте корректный рост

age-correctly-message = Отправьте ваш возраст(г)
age-err-message = Отправьте корректный возраст

register-finish-message =
    <b>Нажмите соответствующую кнопку,если готовы завершить регистрацию</b>

    <b>Ваши данные:</b>
    Пол: {$sex}
    Возраст: {$age}
    Уровень активности: {$activity}
    Вес: {$weight}
    Рост: {$height}
    Язык: {$lang}

    {$calories_exists ->
        [1] <b>Дневной лимит калорий: {$calories}</b>
       *[other] <b>Не удалось вычислить лимит калорий, проверьте указанные данные.</b>
    }
register-finish-button = Завершить регистрацию

menu-message =
    <b>Главное меню.</b>
    Добро пожаловать, {$username}

    {$userGender ->
        [male] добавил
        [female] добавила
       *[other] добавил(а)
    } {$photoCount ->
        [one] одну фотографию
        [few] {$photoCount} новых фотографии
       *[other] {$photoCount} новых фотографий
    } в свой стрим.

next-button = Далее
previous-button = Назад

defautl-parameter = Неопределено