hello-message = <b>Hi!</b>
        This is a bot for monitoring calories consumed.
        Sign up to determine your daily calorie intake and start using the bot.
hello-register = Register

lang-ru = 🇷🇺 Русский
lang-en = 🇬🇧 English

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

register-finish-message =
    <b>Click the appropriate button if you are ready to complete the registration</b>

    <b>Your data:</b>
    Gender: {$sex}
    Age: {$age} y.o.
    Activity level: {$activity}
    Weight: {$weight} kg.
    Height: {$height} cm.
    Language: {$lang}

    {$calories_exists ->
        [1] <b>Daily calorie limit: {$calories} kcal.</b>
       *[other] <b>The calorie limit could not be calculated, check the specified data.</b>
    }

register-finish-button = Complete registration

main-menu-message =
    <b>Main menu.</b>
    <b>Welcome, {$username}!</b>

    <b>Your data:</b>
    <i>Gender:</i> {$sex}
    <i>Age:</i> {$age} y.o.
    <i>Activity level:</i> {$activity}
    <i>Weight:</i> {$weight} kg.
    <i>Height:</i> {$height} cm.
    <i>Language:</i> {$lang}

    <b>Daily calorie limit: {$calories} kcal.</b>

    <b>Received today {$current_calories} out of {$calories} kcal.</b>

subtract-calories = Subtract calories
plus-calories = Add calories

change-data-button = Change the data

next-button = Next
previous-button = Back

defautl-parameter = <i>Undefined</i>