from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    hello: Hello
    lang: Lang
    geo: Geo
    sex: Sex
    activity: Activity
    parameters: Parameters
    weight: Weight
    height: Height
    age: Age
    plus: Plus
    subtract: Subtract
    register: Register
    main: Main
    change: Change
    settings: Settings
    language: Language
    calories: Calories
    next: Next
    previous: Previous
    defautl: Defautl


class Hello:
    @staticmethod
    def message() -> Literal["""&lt;b&gt;Hi!&lt;/b&gt;
This is a bot for monitoring calories consumed.
Sign up to determine your daily calorie intake and start using the bot."""]: ...

    @staticmethod
    def register() -> Literal["""Register"""]: ...


class Lang:
    @staticmethod
    def ru() -> Literal["""🇷🇺 Русский"""]: ...

    @staticmethod
    def en() -> Literal["""🇬🇧 English"""]: ...


class Geo:
    err: GeoErr

    @staticmethod
    def message() -> Literal["""Send your city or the city in which you are located in the time zone in the format: &#34;Country, region, locality&#34;

Or send your time zone in the format: &#34;+HH:MM&#34;
For example: &#34;+03:00&#34;"""]: ...


class GeoErr:
    @staticmethod
    def message() -> Literal["""Incorrect data"""]: ...


class Sex:
    wooman: SexWooman
    man: SexMan

    @staticmethod
    def message() -> Literal["""Choose a gender:"""]: ...


class SexWooman:
    @staticmethod
    def button() -> Literal["""👩🏼 Female"""]: ...


class SexMan:
    @staticmethod
    def button() -> Literal["""👨🏻 Male"""]: ...


class Activity:
    level: ActivityLevel

    @staticmethod
    def message() -> Literal["""Select your activity level:"""]: ...


class ActivityLevel:
    @staticmethod
    def high() -> Literal["""🏃 High activity"""]: ...

    @staticmethod
    def medium() -> Literal["""🚶 Average activity"""]: ...

    @staticmethod
    def low() -> Literal["""🧎 Low activity"""]: ...


class Parameters:
    err: ParametersErr


class ParametersErr:
    @staticmethod
    def message() -> Literal["""Send a text"""]: ...


class Weight:
    correctly: WeightCorrectly
    err: WeightErr


class WeightCorrectly:
    @staticmethod
    def message() -> Literal["""Send your weight (kg)"""]: ...


class WeightErr:
    @staticmethod
    def message() -> Literal["""Send the correct weight"""]: ...


class Height:
    correctly: HeightCorrectly
    err: HeightErr


class HeightCorrectly:
    @staticmethod
    def message() -> Literal["""Send your height (cm)"""]: ...


class HeightErr:
    @staticmethod
    def message() -> Literal["""Send the correct growth"""]: ...


class Age:
    correctly: AgeCorrectly
    err: AgeErr


class AgeCorrectly:
    @staticmethod
    def message() -> Literal["""Send your age"""]: ...


class AgeErr:
    @staticmethod
    def message() -> Literal["""Send the correct age"""]: ...


class Plus:
    calories: PlusCalories


class PlusCalories:
    err: PlusCaloriesErr
    correctly: PlusCaloriesCorrectly

    @staticmethod
    def button() -> Literal["""➕ Add calories"""]: ...


class PlusCaloriesErr:
    @staticmethod
    def message() -> Literal["""Send the correct number"""]: ...


class PlusCaloriesCorrectly:
    @staticmethod
    def message() -> Literal["""&lt;b&gt;Send the number of calories you need to add:&lt;/b&gt;"""]: ...


class Subtract:
    calories: SubtractCalories


class SubtractCalories:
    err: SubtractCaloriesErr
    correctly: SubtractCaloriesCorrectly

    @staticmethod
    def button() -> Literal["""➖ Subtract calories"""]: ...


class SubtractCaloriesErr:
    @staticmethod
    def message() -> Literal["""Send the correct number"""]: ...


class SubtractCaloriesCorrectly:
    @staticmethod
    def message() -> Literal["""&lt;b&gt;Send the number of calories you need to substract:&lt;/b&gt;"""]: ...


class Register:
    finish: RegisterFinish


class RegisterFinish:
    @staticmethod
    def message(*, sex, age, activity, weight, height, timezone, lang) -> Literal["""&lt;b&gt;Click the appropriate button if you are ready to complete the registration&lt;/b&gt;

&lt;b&gt;Your data:&lt;/b&gt;
&lt;i&gt;Gender:&lt;/i&gt; { $sex }
&lt;i&gt;Age:&lt;/i&gt; { $age } y.o.
&lt;i&gt;Activity level:&lt;/i&gt; { $activity }
&lt;i&gt;Weight:&lt;/i&gt; { $weight } kg.
&lt;i&gt;Height:&lt;/i&gt; { $height } cm.
&lt;i&gt;Time zone:&lt;/i&gt; { $timezone }
&lt;i&gt;Language:&lt;/i&gt; { $lang }

"""]: ...

    @staticmethod
    def button() -> Literal["""Complete registration ☑️"""]: ...


class Main:
    menu: MainMenu


class MainMenu:
    @staticmethod
    def message(*, username, sex, age, activity, weight, height, calories, current_calories, calories, lang, timezone) -> Literal["""&lt;b&gt;Main menu.&lt;/b&gt;
&lt;b&gt;Welcome, { $username }!&lt;/b&gt;

&lt;b&gt;Your data:&lt;/b&gt;
&lt;i&gt;Gender:&lt;/i&gt; { $sex }
&lt;i&gt;Age:&lt;/i&gt; { $age } y.o.
&lt;i&gt;Activity level:&lt;/i&gt; { $activity }
&lt;i&gt;Weight:&lt;/i&gt; { $weight } kg.
&lt;i&gt;Height:&lt;/i&gt; { $height } cm.

&lt;b&gt;Daily calorie limit: { $calories } kcal.&lt;/b&gt;

&lt;b&gt;Received today { $current_calories } out of { $calories } kcal.&lt;/b&gt;
&lt;b&gt;{ $lang } / { $timezone }&lt;/b&gt;"""]: ...


class Change:
    data: ChangeData


class ChangeData:
    menu: ChangeDataMenu
    sex: ChangeDataSex
    age: ChangeDataAge
    activity: ChangeDataActivity
    weight: ChangeDataWeight
    height: ChangeDataHeight
    calories: ChangeDataCalories
    save: ChangeDataSave

    @staticmethod
    def button() -> Literal["""💆 Change the data"""]: ...


class ChangeDataMenu:
    @staticmethod
    def message() -> Literal["""&lt;b&gt;Change the data:&lt;/b&gt;"""]: ...


class ChangeDataSex:
    @staticmethod
    def button() -> Literal["""👨🏻 Change the gender 👩🏼"""]: ...

    @staticmethod
    def message() -> Literal["""&lt;b&gt;Choose a gender:&lt;/b&gt;"""]: ...


class ChangeDataAge:
    @staticmethod
    def button() -> Literal["""⏳ Change age"""]: ...

    @staticmethod
    def message() -> Literal["""&lt;b&gt;Send new age:&lt;/b&gt;"""]: ...


class ChangeDataActivity:
    @staticmethod
    def button() -> Literal["""🏃 Change the activity level"""]: ...

    @staticmethod
    def message() -> Literal["""&lt;b&gt;Select the activity level:&lt;/b&gt;"""]: ...


class ChangeDataWeight:
    @staticmethod
    def button() -> Literal["""⚖️ Change the weight"""]: ...

    @staticmethod
    def message() -> Literal["""&lt;b&gt;Send weight:&lt;/b&gt;"""]: ...


class ChangeDataHeight:
    @staticmethod
    def button() -> Literal["""📐 Change the height"""]: ...

    @staticmethod
    def message() -> Literal["""&lt;b&gt;Send height:&lt;/b&gt;"""]: ...


class ChangeDataCalories:
    @staticmethod
    def button() -> Literal["""🔧 Set the calorie limit manually"""]: ...

    @staticmethod
    def message() -> Literal["""With manual installation, automatic calorie recalculation is disabled when personal parameters are changed.
You can turn it on again in &lt;b&gt;settings&lt;/b&gt;

&lt;b&gt;Send the number of calories:&lt;/b&gt;"""]: ...


class ChangeDataSave:
    update: ChangeDataSaveUpdate


class ChangeDataSaveUpdate:
    @staticmethod
    def calories() -> Literal["""✔️ Save and update calories"""]: ...


class Settings:
    @staticmethod
    def button() -> Literal["""🛠 Settings"""]: ...

    @staticmethod
    def message() -> Literal["""&lt;b&gt;Settings:&lt;/b&gt;"""]: ...


class Language:
    change: LanguageChange


class LanguageChange:
    @staticmethod
    def button() -> Literal["""🌍 Change the language"""]: ...

    @staticmethod
    def message() -> Literal["""&lt;b&gt;Select a language:&lt;/b&gt;"""]: ...


class Calories:
    counting: CaloriesCounting


class CaloriesCounting:
    @staticmethod
    def on() -> Literal["""[ ✔️ ] Auto-calorie counting (Enabled)"""]: ...

    @staticmethod
    def off() -> Literal["""[    ] Auto-calorie counting (Disabled)"""]: ...


class Next:
    @staticmethod
    def button() -> Literal["""Next ➡️"""]: ...


class Previous:
    @staticmethod
    def button() -> Literal["""⬅️ Previous"""]: ...


class Defautl:
    @staticmethod
    def parameter() -> Literal["""&lt;i&gt;Undefined&lt;/i&gt;"""]: ...

    @staticmethod
    def timezone() -> Literal["""00:00"""]: ...

