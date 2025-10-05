class BaseClass:
    def __init__(self):
        self._protected = 'Protected'
        self.__private = 'Private'

    def _protected_method(self):
        print('This is a protected method')
    
    def __private_method(self):
        print('This is a private method')

    def public_method(self):
        self.__private_method()

base = BaseClass()

print(base._protected) # Result: 'Protected'
print(base.__private) # Result: Error

base.public_method() # Result: 'This is a private method'
base._protected_method() # Result: 'This is a protected method'
base.__private_method() # Result: Error