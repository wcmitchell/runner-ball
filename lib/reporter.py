class Reporter():
    def __init__(self, **kwargs):
        self.title = kwargs.get("title")
        self.data = kwargs.get("data")

    def report(self):
        print(f"\n====== {self.title} ======")
        for k,v in self.data.items():
            print(f"{k:20}{v}")
