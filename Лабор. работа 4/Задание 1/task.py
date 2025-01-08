# TODO: описать базовый класс
class Evergreen:
    """
    Базовый класс для хвойных деревьев

    Attributes:
        crown (str): Вид кроны дерева (например, овальная, конусообразная)
        cone (str): Вид шишки дерева (например, удлиненная, округлая)
        tone (str): Цвет (оттенок) хвои (например, темный, светлый)
    """

    def __init__(self, crown: str, cone: str, tone: str):
        self._crown = crown
        self._cone = cone
        self._tone = tone

    @property
    def crown(self) -> str:
        return self._crown

    @property
    def cone(self) -> str:
        return self._cone

    @property
    def tone(self) -> str:
        return self._tone

    def __str__(self) -> str:
        return f"{self.crown} {self.cone} {self.tone}"

    def __repr__(self) -> str:
        return f"Evergreen(crown={self.crown!r}, pinecone={self.cone!r}, tone={self.tone!r})"


# TODO: описать дочерний класс
class Pine(Evergreen):
    """
    Дочерний класс для хвойных деревьев

    Attributes:
        crown (str): Вид кроны дерева (унаследовано)
        cone (str): Вид шишки дерева (унаследовано)
        tone (str): Цвет (оттенок) хвои (унаследовано)
        height (int, float): Высота дерева
    """

    def __init__(self, crown: str, cone: str, tone: str, height: (int, float)):
        super().__init__(crown, cone, tone)
        self.height = height

    @property
    def height(self) -> (int, float):
        return self._height

    @height.setter
    def height(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError('Высота дерева должна быть целым числом или числом с плавающей точкой')
        if value <= 0:
            raise ValueError('Высота дерева должна быть больше нуля')
        self._height = value

    def __str__(self) -> str:
        return f"{self.crown} {self.cone} {self.tone} Высота: {self._height:.2f} м"

    def cut_down_tree(self) -> str:
        """
        Срубает дерево

        Returns:
             str: Строка, обозначающая срубку дерева.
        """
        return "Дерево срублено"

    def plant_tree(self) -> str:
        """
        Сажает дерево

        Returns:
             str: Строка, обозначающая посадку дерева.
        """
        return "Дерево посажено"

    def condition(self) -> str:
        """
        Перегрузка метода состояния.
        Метод различается для разных видов хвойных деревьев.
        Returns:
             str: Строка, обозначающее состояние дерева
        """
        return "На севере диком стоит одиноко..."
