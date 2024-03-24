from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    hello: Hello
    lang: Lang
    sex: Sex
    activity: Activity
    parameters: Parameters
    weight: Weight
    height: Height
    age: Age
    register: Register
    main: Main
    subtract: Subtract
    plus: Plus
    change: Change
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


class Register:
    finish: RegisterFinish


class RegisterFinish:
    @staticmethod
    def message(*, sex, age, activity, weight, height, lang) -> Literal["""&lt;b&gt;Click the appropriate button if you are ready to complete the registration&lt;/b&gt;

&lt;b&gt;Your data:&lt;/b&gt;
Gender: { $sex }
Age: { $age } y.o.
Activity level: { $activity }
Weight: { $weight } kg.
Height: { $height } cm.
Language: { $lang }

"""]: ...

    @staticmethod
    def button() -> Literal["""Complete registration"""]: ...


class Main:
    menu: MainMenu


class MainMenu:
    @staticmethod
    def message(*, username, sex, age, activity, weight, height, lang, calories, current_calories, calories) -> Literal["""&lt;b&gt;Main menu.&lt;/b&gt;
&lt;b&gt;Welcome, { $username }!&lt;/b&gt;

&lt;b&gt;Your data:&lt;/b&gt;
&lt;i&gt;Gender:&lt;/i&gt; { $sex }
&lt;i&gt;Age:&lt;/i&gt; { $age } y.o.
&lt;i&gt;Activity level:&lt;/i&gt; { $activity }
&lt;i&gt;Weight:&lt;/i&gt; { $weight } kg.
&lt;i&gt;Height:&lt;/i&gt; { $height } cm.
&lt;i&gt;Language:&lt;/i&gt; { $lang }

&lt;b&gt;Daily calorie limit: { $calories } kcal.&lt;/b&gt;

&lt;b&gt;Received today { $current_calories } out of { $calories } kcal.&lt;/b&gt;"""]: ...


class Subtract:
    @staticmethod
    def calories() -> Literal["""Subtract calories"""]: ...


class Plus:
    @staticmethod
    def calories() -> Literal["""Add calories"""]: ...


class Change:
    data: ChangeData


class ChangeData:
    @staticmethod
    def button() -> Literal["""Change the data"""]: ...


class Next:
    @staticmethod
    def button() -> Literal["""Next"""]: ...


class Previous:
    @staticmethod
    def button() -> Literal["""Back"""]: ...


class Defautl:
    @staticmethod
    def parameter() -> Literal["""&lt;i&gt;Undefined&lt;/i&gt;"""]: ...

