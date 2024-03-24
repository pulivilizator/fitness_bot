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

weight-correctly-message = Отправьте ваш вес (кг)
weight-err-message = Отправьте корректный вес

height-correctly-message = Отправьте ваш рост (см)
height-err-message = Отправьте корректный рост

age-correctly-message = Отправьте ваш возраст
age-err-message = Отправьте корректный возраст

register-finish-message =
    <b>Нажмите соответствующую кнопку, если готовы завершить регистрацию</b>

    <b>Ваши данные:</b>
    <i>Пол:</i> {$sex}
    <i>Возраст:</i> {$age ->
                    [one] {$age} год
                    [few] {$age} года
                    *[other] {$age} лет
                    }
    <i>Уровень активности:</i> {$activity}
    <i>Вес:</i> {$weight} кг.
    <i>Рост:</i> {$height} см.
    <i>Язык:</i> {$lang}

    {$calories_exists ->
        [1] <b>Дневной лимит калорий: {$calories} ккал.</b>
       *[other] <b>Не удалось вычислить лимит калорий, проверьте указанные данные.</b>
    }
register-finish-button = Завершить регистрацию

main-menu-message =
    <b>Главное меню.</b>
    <b>Добро пожаловать, {$username}!</b>

    <b>Ваши данные:</b>
    <i>Пол:</i> {$sex}
    <i>Возраст:</i> {$age ->
                    [one] {$age} год
                    [few] {$age} года
                    *[other] {$age} лет
                    }
    <i>Уровень активности:</i> {$activity}
    <i>Вес:</i> {$weight} кг.
    <i>Рост:</i> {$height} см.
    <i>Язык:</i> {$lang}

    <b>Дневной лимит калорий: {$calories} ккал.</b>

    <b>Получено сегодня {$current_calories} из {$calories} ккал.</b>

subtract-calories = Вычесть калории
plus-calories = Прибавить калории

change-data-button = Изменить данные

next-button = Далее
previous-button = Назад

defautl-parameter = <i>Неопределено</i>