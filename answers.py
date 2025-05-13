class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = 100  # battery starts fully charged

    def make_call(self, number):
        print(f"Calling {number} from {self.model}... 📞")

    def charge(self):
        self.battery = 100
        print(f"{self.model} is now fully charged! 🔋")

    def get_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage."
