class DigitalCounter:
    def __init__(self, begin, end, state=None):
        self.begin = begin
        self.end = end
        if state == None:
            self.state = begin
        else:
            self.state = state

        self.is_last_operation_up = None

    def up(self):
        if self.state < self.end:
            self.state += 1
        else:
            self.state = self.begin

        self.is_last_operation_up = True

    def down(self):
        if self.state > self.begin:
            self.state -= 1 
        else: 
            self.state = self.end

        self.is_last_operation_up = False

    def get_value(self):
        return self.state
    
    def is_last_operation_up(self):
        return self.is_last_operation_up
    

value = 0
begin = 0
end = 999


point = DigitalCounter(begin, end, value)
print(point.get_value())

point.down()
point.down()
print(point.is_last_operation_up)
point.up()
print(point.is_last_operation_up)

print(point.get_value())    
