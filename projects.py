class Project:
    def __init__(self, proj_name, init_date, end_date, elapsed_time, elapsed_value,emp_id) -> None:
        self.__projName = proj_name
        self.initDate = init_date
        self.endDate = end_date
        self.elapsedTime = elapsed_time
        self.elapsedValue = elapsed_value
        self.employeeId = emp_id
    
    @property
    def projectName(self):
        return self.__projName


    @property
    def initDate(self):
        return self._initDate
    @initDate.setter
    def initDate(self, new_initDate):
        self._initDate = new_initDate

    @property
    def endDate(self):
        return self._endDate
    @endDate.setter
    def endDate(self,new_endDate):
        self._endDate = new_endDate

    @property
    def elapsedTime(self):
        return self._elapsedTime
    @elapsedTime.setter
    def elapsedTime(self, new_elapsedTime):
        self._elapsedTime = new_elapsedTime

    @property
    def elapsedValue(self):
        return self._elapsedTime
    @elapsedValue.setter
    def elapsedValue(self, new_elapsedValue):
        self._elapsedValue = new_elapsedValue

    @property
    def employeeId(self):
        return self._employeeId
    @employeeId.setter
    def employeeID(self, new_employeeID):
        self._employeeId = new_employeeID
            