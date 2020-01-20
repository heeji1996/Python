
## myCal 파일
class Calculator3:
    def __init__(self):
        self.result = 0

    def sum(self,num, num2 = None):  # 메서드 오버로딩 개념대신 이렇게 활용가능
        if num2 == None:
            self.result += num
            return self.result
        else:
            self.result = num + num2
            return self.result

    def sub(self,num,num2 = None):  # 메서드 오버로딩 개념
        if num2 == None:
            self.result -= num
            return self.result
        else:
            self.result = num - num2
            return self.result

    def mul(self,num,num2 = None):  # 메서드 오버로딩 개념
        if num2 == None:
            self.result *= num
            return self.result
        else:
            self.result = num * num2
            return self.result

    def div(self,num,num2 = None): # 메서드 오버로딩 개념
        if num2 == None:
            self.result /= num
            return self.result
        else:
            self.result = num / num2
            return self.result