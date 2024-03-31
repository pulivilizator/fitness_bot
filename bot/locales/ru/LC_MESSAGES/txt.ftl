hello-message = <b>Привет!</b>
        Это бот для контроля потребляемых калорий.
        Зарегистрируйся чтобы определить твою суточную норму калорий и начать пользоваться ботом.
hello-register = Зарегистрироваться

lang-ru = 🇷🇺 Русский
lang-en = 🇬🇧 English

geo-message = Отправьте свой город или город, в часовом поясе которого вы находитесь, в формате: "Страна, регион, населенный пункт"

              Либо отправьте ваш часовой пояс в формате: "+ЧЧ:ММ"
              Например: "+03:00"
geo-err-message = Некорректные данные

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

plus-calories-err-message = Отправьте корректное число
plus-calories-correctly-message = <b>Отправьте число калорий, которые необходимо прибавить:</b>

subtract-calories-err-message = Отправьте корректное число
subtract-calories-correctly-message = <b>Отправьте число калорий, которые необходимо вычесть:</b>

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
    <i>Часовой пояс</i>: {$timezone}
    <i>Язык:</i> {$lang}

    {$calories_exists ->
        [1] <b>Дневной лимит калорий: {$calories} ккал.</b>
       *[other] <b>Не удалось вычислить лимит калорий, проверьте указанные данные.</b>
    }
register-finish-button = Завершить регистрацию ☑️

main-menu-message =
    <b>Главное меню.</b>
    <b>Добро пожаловать, {$username}!</b> 💫

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

    <b>Дневной лимит калорий: {$calories} ккал.</b>

    <b>Получено сегодня {$current_calories} из {$calories} ккал.</b>
    <b>{$lang} / UTC {$timezone}</b>

subtract-calories-button = ➖ Вычесть калории
plus-calories-button = ➕ Прибавить калории

change-data-button = 💆 Изменить данные
change-data-menu-message = <b>Изменить данные:</b>

change-data-sex-button = 👨🏻 Изменить пол 👩🏼
change-data-sex-message = <b>Выберите пол:</b>

change-data-age-button = ⏳ Изменить возраст
change-data-age-message = <b>Отправьте новый возраст:</b>

change-data-activity-button = 🏃 Изменить уровень активности
change-data-activity-message = <b>Выберите уровень активности:</b>

change-data-weight-button = ⚖️ Изменить вес
change-data-weight-message = <b>Отправьте вес:</b>

change-data-height-button = 📐 Изменить рост
change-data-height-message = <b>Отправьте рост:</b>

change-data-calories-button = 🔧 Установить количество калорий вручную
change-data-calories-message = При ручной установке, автоматический пересчет калорий при изменении личных параметров отключается.
                               Снова включить его вы можете в <b>настройках</b>

                               <b>Отправьте количество калорий:</b>

change-data-save-update-calories = ✔️ Сохранить и обновить калории

settings-button = 🛠 Настройки
settings-message = <b>Настройки:</b>

language-change-button = 🌍 Сменить язык
language-change-message = <b>Выберите язык:</b>

calories-counting-on = [ ✔️ ] Автоподсчет калорий (Включено)
calories-counting-off = [    ] Автоподсчет калорий (Отключено)

next-button = Далее ➡️
previous-button = ⬅️ Назад

defautl-parameter = <i>Неопределено</i>
defautl-timezone = 00:00