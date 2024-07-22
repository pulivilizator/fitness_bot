hello-message = <b>Hi!</b>
        This is a bot for monitoring calories consumed.
        Sign up to determine your daily calorie intake and start using the bot.
hello-register = Register

lang-ru = 🇷🇺 Русский
lang-en = 🇬🇧 English

geo-message = Send your city or the city in which you are located in the time zone in the format: <b>"Country, region, locality"</b>
              Or send your time zone in the format: <b>"+HH:MM"</b>
              For example: <b>"+03:00"</b>

              This is necessary to automatically reset the calories to zero when the next day arrives.
geo-err-message = Incorrect data


sex-message = Choose a gender:
sex-wooman-button = 👩🏼 Female
sex-man-button = 👨🏻 Male

activity-message = Select your activity level:
activity-level-high = 🏃 High activity
activity-level-medium = 🚶 Average activity
activity-level-low = 🧎 Low activity

parameters-err-message = Send a text

weight-correctly-message = Send your weight (kg)
weight-err-message = Send the correct weight

height-correctly-message = Send your height (cm)
height-err-message = Send the correct growth

age-correctly-message = Send your age
age-err-message = Send the correct age

plus-calories-err-message = Send the correct number
plus-calories-correctly-message = <b>Send the number of calories you need to add:</b>

subtract-calories-err-message = Send the correct number
subtract-calories-correctly-message = <b>Send the number of calories you need to substract:</b>

register-finish-message =
    <b>Click the appropriate button if you are ready to complete the registration</b>

    <b>Your data:</b>
    <i>Gender:</i> {$sex}
    <i>Age:</i> {$age} y.o.
    <i>Activity level:</i> {$activity}
    <i>Weight:</i> {$weight} kg.
    <i>Height:</i> {$height} cm.
    <i>Time zone:</i> {$timezone}
    <i>Language:</i> {$lang}

    {$calories_exists ->
        [1] <b>Daily calorie limit: {$calories} kcal.</b>
       *[other] <b>The calorie limit could not be calculated, check the specified data.</b>
    }

register-finish-button = Complete registration ☑️

main-menu-message =
    <b>Main menu.</b>
    <b>Welcome, {$username}!</b>

    <b>Your data:</b>
    <i>Gender:</i> {$sex}
    <i>Age:</i> {$age} y.o.
    <i>Activity level:</i> {$activity}
    <i>Weight:</i> {$weight} kg.
    <i>Height:</i> {$height} cm.

    <b>Daily calorie limit: {$calories} kcal.</b>

    <b>Received today {$current_calories} out of {$calories} kcal.</b>
    <b>{$lang} / UTC {$timezone}</b>

subtract-calories-button = ➖
plus-calories-button = ➕

change-data-button = 💆 Change the data
change-data-menu-message = <b>Change the data:</b>

change-data-sex-button = 👨🏻 Change the gender 👩🏼
change-data-sex-message = <b>Choose a gender:</b>

change-data-age-button = ⏳ Change age
change-data-age-message = <b>Send new age:</b>

change-data-activity-button = 🏃 Change the activity level
change-data-activity-message = <b>Select the activity level:</b>

change-data-weight-button = ⚖️ Change the weight
change-data-weight-message = <b>Send weight:</b>

change-data-height-button = 📐 Change the height
change-data-height-message = <b>Send height:</b>

change-data-calories-button = 🔧 Set the calorie limit manually
change-data-calories-message = With manual installation, automatic calorie recalculation is disabled when personal parameters are changed.
                               You can turn it on again in <b>settings</b>

                               <b>Send the number of calories:</b>

change-data-save-update-calories = ✔️ Save and update calories

settings-button = 🛠 Settings
settings-message = <b>Settings:</b>

language-change-button = 🌍 Change the language
language-change-message = <b>Select a language:</b>

calories-counting-on = [ ✔️ ] Auto-calorie counting (Enabled)
calories-counting-off = [    ] Auto-calorie counting (Disabled)

next-button = Next ➡️
previous-button = ⬅️ Previous

defautl-parameter = <i>Undefined</i>
defautl-timezone = 00:00