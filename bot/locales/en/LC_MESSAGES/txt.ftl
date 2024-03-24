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

weight-correctly-message = Send your weight(kg)
weight-err-message = Send the correct weight

height-correctly-message = Send your height(cm)
height-err-message = Send the correct growth

age-correctly-message = Send your age(d)
age-err-message = Send the correct age

register-finish-message =
    <b>Click the appropriate button if you are ready to complete the registration</b>

    <b>Your data:</b>
    Gender: {$sex}
    Age: {$age}
    Activity level: {$activity}
    Weight: {$weight}
    Height: {$height}
    Language: {$lang}

    {$calories_exists ->
        [1] <b>Daily calorie limit: {$calories}</b>
       *[other] <b>The calorie limit could not be calculated, check the specified data.</b>
    }

register-finish-button = Complete registration

menu-message =
    <b>Main menu.</b>
    Welcome, {$username}

    {$userGender ->
        [male] added
        [female] added
       *[other] added(a)
    } {$photoCount ->
        [one] one photo
        [few] {$photoCount} new photos
       *[other] {$photoCount} new photos
    } to your stream.

next-button = Next
previous-button = Back

defautl-parameter = Undefined