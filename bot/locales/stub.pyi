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
    menu: Menu
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
    def message() -> Literal["""Send your weight(kg)"""]: ...


class WeightErr:
    @staticmethod
    def message() -> Literal["""Send the correct weight"""]: ...


class Height:
    correctly: HeightCorrectly
    err: HeightErr


class HeightCorrectly:
    @staticmethod
    def message() -> Literal["""Send your height(cm)"""]: ...


class HeightErr:
    @staticmethod
    def message() -> Literal["""Send the correct growth"""]: ...


class Age:
    correctly: AgeCorrectly
    err: AgeErr


class AgeCorrectly:
    @staticmethod
    def message() -> Literal["""Send your age(d)"""]: ...


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
Age: { $age }
Activity level: { $activity }
Weight: { $weight }
Height: { $height }
Language: { $lang }

"""]: ...

    @staticmethod
    def button() -> Literal["""Complete registration"""]: ...


class Menu:
    @staticmethod
    def message(*, username) -> Literal["""&lt;b&gt;Main menu.&lt;/b&gt;
Welcome, { $username }

  to your stream."""]: ...


class Next:
    @staticmethod
    def button() -> Literal["""Next"""]: ...


class Previous:
    @staticmethod
    def button() -> Literal["""Back"""]: ...


class Defautl:
    @staticmethod
    def parameter() -> Literal["""Undefined"""]: ...

