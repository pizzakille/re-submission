# re-submission
class Person(ABC):
    def __init__(self, name, id_number):
        self._name = name  # Encapsulation
        self._id = id_number

    @abstractmethod
    def display_role(self):
        pass

# Inheritance
class Doctor(Person):
    def __init__(self, name, id_number, specialization):
        super().__init__(name, id_number)
        self.specialization = specialization

    def display_role(self):
        return f"Doctor: {self._name}, Specialization: {self.specialization}"

class Patient(Person):
    def display_role(self):
        return f"Patient: {self._name}, ID: {self._id}"
