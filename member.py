class Member:
    def __init__(self, member_id, name, email, phone):
        self._member_id = member_id
        self.name = name  # Uses setter
        self.email = email  # Uses setter
        self._phone = phone

    # Member ID - Read Only
    @property
    def member_id(self):
        return self._member_id

    # Name Property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty!")
        self._name = value.strip()

    # Email Property
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Email must contain '@' symbol!")
        self._email = value.lower()

    # Phone Property
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value or not value.strip():
            raise ValueError("Phone number cannot be empty!")
        self._phone = value.strip()

    def __str__(self):
        return f"ID: {self._member_id} | Name: {self._name} | Email: {self._email} | Phone: {self._phone}"