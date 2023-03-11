"""
Contains back-end classes for main.py
"""


class Street:
    """
    Stores information about streets

    >>> kozelnytska = Street('Kozelnytska str')
    >>> kozelnytska.set_description('Kozelnytska str')

    >>> stryiska = Street('Stryiska str')
    >>> stryiska.set_description('Stryiska str')

    >>> stryiska.description
    'Stryiska str'

    >>> kozelnytska.link_street(stryiska, 'west')
    >>> kozelnytska.move('west').name
    'Stryiska str'
    """
    def __init__(self, name):
        """
        Initializes data
        :param name:
        """
        self.item = None
        self.person = None
        self.description = None
        self.name = name
        self.street_dct = dict()

    def set_description(self, description: str):
        """
        Sets description for particular street
        :param description:
        :return:
        """
        self.description = description
        return None

    def link_street(self, street: object, side: str):
        """
        Links street to another street according to the globe side
        :param street:
        :param side:
        :return:
        """
        self.street_dct.update({side: street})
        return None

    def set_character(self, person: object):
        """
        Sets character who is on the street
        :param person:
        :return:
        """
        self.person = person
        return None

    def set_item(self, item: object):
        """
        Sets item which is on the street
        :param item:
        :return:
        """
        self.item = item
        return None

    def get_details(self):
        """
        Displays details about street
        :return:
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for side in list(self.street_dct.keys()):
            print(f"The {self.street_dct[side].name} is {side}")
        return None

    def get_person(self):
        """
        Returns character who is on the street
        :return:
        """
        return self.person

    def get_item(self):
        """
        Returns item which is on the street
        :return:
        """
        return self.item

    def move(self, side: str):
        """
        Moves to another street
        :param side:
        :return:
        """
        return self.street_dct[side]


class Person:
    """
    Stores information about particular character

    >>> zbui = Enemy('Zbui', 'Robber, burglar')
    >>> zbui.set_description('Yesterday was a lotr')

    >>> zbui.describe()
    Zbui is here!
    Robber, burglar
    """
    def __init__(self, name, tipe):
        """
        Initializes data
        :param name:
        :param tipe:
        """
        self.description = None
        self.name = name
        self.type = tipe

    def set_description(self, description: str):
        """
        Sets description for the character
        :param description:
        :return:
        """
        self.description = description
        return None

    def describe(self):
        """
        Displays description of the character
        :return:
        """
        print(f"{self.name} is here!")
        print(self.type)
        return None


class Enemy(Person):
    """
    Stores information about enemy

    >>> lotr = Enemy('Lotr', 'Scoundrel, robber, plunderer')
    >>> lotr.set_description('Cheap clothes and a sly smile')

    >>> lotr.describe()
    Lotr is here!
    Scoundrel, robber, plunderer
    """
    def __init__(self, name, tipe):
        """
        Initializes and inherits data
        :param name:
        :param tipe:
        """
        self.weakness = None
        self.treat = None
        super().__init__(name, tipe)

    def set_weakness(self, weakness: str):
        """
        Sets weakness of the particular enemy
        :param weakness:
        :return:
        """
        self.weakness = weakness
        return None

    def fight(self, fight_with: str):
        """
        Starts fight with enemy
        Returns True of False according to the result
        :param fight_with:
        :return:
        """
        if fight_with == self.weakness:
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False


class Friend(Person):
    """
    Stores information about friend

    >>> kavaler = Friend('Kavaler', 'A man entertaining a woman')
    >>> kavaler.set_description('Young, rich, handsome')
    >>> kavaler.describe()
    Kavaler is here!
    A man entertaining a woman
    """
    def __init__(self, name, tipe):
        """
        Initializes and inherits data
        :param name:
        :param tipe:
        """
        self.treat = None
        self.weakness = None
        super().__init__(name, tipe)

    def set_treat(self, treat: str):
        """
        Sets treat for a particular friend
        :param treat:
        :return:
        """
        self.treat = treat
        return None

    def make_treatment(self, treat_with: str):
        """
        Returns True of False according to the reat
        :param treat_with:
        :return:
        """
        if treat_with == self.treat:
            return True
        return False


class Item:
    """
    Describes particular item

    >>> gun = Weapon('gun')
    >>> gun.set_description('loaded')
    >>> gun.description
    'loaded'
    """
    def __init__(self, name):
        """
        Initializes data
        :param name:
        """
        self.description = None
        self.name = name

    def set_description(self, description):
        """
        Sets description of the item
        :param description:
        :return:
        """
        self.description = description
        return None

    def get_name(self):
        """
        Returns item's name
        :return:
        """
        return self.name


class Weapon(Item):
    """
    Describes weapons

    >>> knife = Weapon('knife')
    >>> knife.set_description('sharp')
    >>> knife.describe()
    Weapon
    The [knife] is here - sharp
    """
    def __init__(self, name):
        """
        Inherits data
        :param name:
        """
        super().__init__(name)

    def describe(self):
        """
        Displays description of the item
        :return:
        """
        print('Weapon')
        print(f"The [{self.name}] is here - {self.description}")
        return None


class Treat(Item):
    """
    Describes treats

    >>> shokolad = Treat('chocolate')
    >>> shokolad.set_description('Qualifying')
    >>> shokolad.describe()
    Treat
    The [chocolate] is here - Qualifying
    """
    def __init__(self, name):
        """
        Inherits data
        :param name:
        """
        super().__init__(name)

    def describe(self):
        """
        Displays description of the item
        :return:
        """
        print('Treat')
        print(f"The [{self.name}] is here - {self.description}")
        return None
