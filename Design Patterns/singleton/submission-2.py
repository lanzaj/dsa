class Singleton:
    _is_init = None
    value = ""

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._is_init == None:
            cls._is_init = super(Singleton, cls).__new__(cls)
        return cls._is_init

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
