class Employee:
    def __init__(self, id, n, salary):
        self.__id = id
        self.name = n
        self.salary = salary
    
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary
    
    
