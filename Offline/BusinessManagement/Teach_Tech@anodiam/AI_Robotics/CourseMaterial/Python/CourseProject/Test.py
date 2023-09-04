class MyClass:
    def instance_method(self, arg1, arg2):
        # Access instance attributes using self
        self.attribute = arg1 + arg2
        return self.attribute


class MyClass:
    class_attribute = 10

    @classmethod
    def class_method(cls, arg1):
        cls.class_attribute += arg1
        return cls.class_attribute


class MyClass:
    @staticmethod
    def static_method(arg1, arg2):
        return arg1 * arg2
