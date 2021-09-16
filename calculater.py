operator_priority = {'+':int(0),'-':int(0),'*':int(1),'/':int(1),'^':int(2),'MAX':int(3)}
operator = ('+','-','*','/','^')
number = ('0','1','2','3','4','5','6','7','8','9')
class Node:
    def __init__(self,data):
        self.data = data
    def result(self):
        pass
    def display(self):
        pass

class Test_Node(Node):
    def result(self):
        return "TEST"

class Operator_Node(Node):
    def __init__(self,data):
        self.front_node = None
        self.back_node = None
        self.bracket = 0
        self.data = data
    def display(self):
        print(self.data)
        self.front_node.display()
        self.back_node.display()
    def priority(self):
        return operator_priority[self.data] + self.bracket * operator_priority['MAX']
    def full(self):
        if self.front_node == None :
            return False
        if self.back_node == None:
            return False
        return True,
    def result(self):
        if self.front_node ==None:
            print("앞의노드없음오류발생")
            return float(0)
        if self.back_node == None:
            print("뒤의노드없음오류발생")
            return float(0)
        if self.data=='+':
            return self.front_node.result()+ self.back_node.result()
        elif self.data=='-':
            return self.front_node.result()- self.back_node.result()
        elif self.data=='*':
            return self.front_node.result()* self.back_node.result()
        elif self.data=='/':
            return self.front_node.result()/ self.back_node.result()
        elif self.data=='^':
            return self.front_node.result()** self.back_node.result()
        else:
            print("연산자없음오류발생")
            return float(0)

class Number_Node(Node):
    def __init__(self,data):
        self.negative = False
        self.data = data
    def display(self):
        print(self.data)
    def result(self):
        if self.negative:
            return float(self.data) * float(-1)
        else :
            return float(self.data)

class Calculator:

    def __init__(self):
        self.number_buffer = ''
        self.operator_stack = []
        self.data_stack = []
        self.root_node= None
        self.negative = False
        self.dot = False
        self.bracket = 0
        self.start()
        
    def start(self):
        print("계산기 작동")
        while True:
            data = input()
            self.input_line(data = data)
            

    def input_line(self,data):
        #계산기 설정초기화
        self.operator_stack = []
        self.data_stack = []
        self.negative = False
        self.dot = False
        for e in data :#라인 스캔
            self.input_char(char=e)
        self.end()
        print('.')
        print(self.root_node.result())
        return True

    def input_char(self,char):
        if char in number:#넘버 버퍼에 연산자가 나올때까지 숫자저장
            self.number_buffer  = self.number_buffer + char;
        elif char in operator:
            self.input_operator(operator=char)
        elif char == '.':#.은 한번만 사용가능
            if self.dot == False:
                self.number_buffer  = self.number_buffer + char;
                self.dot = True
        elif char == ' ':# 띄우는건 기능없음
            a = 1
        elif char=='(':
            self.bracket +=1
        elif char==')':
            self.bracket -=1
        else:# 다른문자입력시 오류
            return False

    def input_operator(self,operator):
        operator_node = Operator_Node(data=operator)
        operator_node.bracket = self.bracket
        front_operator_node = None
        data_node = None
        front_data_node = None
        if self.number_buffer=='':
            if self.root_node == None:
                if operator == '-':
                    self.negative = True
                    return True
                else:
                    print('연속 연산자오류')
                    return False # 오류발생
            else:
                data_node = self.root_node # 루트노드를 데이터로쓰기
                self.root_node = None
        else:
            data_node = self.number_node_create()
        while True:
            print('.',end='')
            if len(self.operator_stack)==0:
                break
            if len(self.data_stack)==0:
                break
            front_operator_node = self.operator_stack[-1]
            front_data_node = self.data_stack[-1]
            if operator_node.priority()> front_operator_node.priority():
                break
            else:
                self.operator_stack.remove(front_operator_node)
                self.data_stack.remove(front_data_node)
                front_operator_node.front_node = front_data_node
                front_operator_node.back_node = data_node
                data_node = front_operator_node

        self.data_stack.append(data_node)
        self.operator_stack.append(operator_node)

    def number_node_create(self):
        result = Number_Node(self.number_buffer)
        result.negative = self.negative
        self.dot = False
        self.Negative = False
        self.number_buffer = ''
        return result

    def end(self):
        operator_node = None
        data_node = None
        front_data_node = None
        if self.number_buffer=='':
            return False #오류
        else :
            data_node = self.number_node_create()
        while True: 
            print('.',end='')
            if len(self.operator_stack)==0:
                break #오류
            if len(self.data_stack)==0:
                return False #오류
            operator_node = self.operator_stack[-1]
            front_data_node = self.data_stack[-1]
            self.operator_stack.remove(operator_node)
            self.data_stack.remove(front_data_node)
            operator_node.front_node = front_data_node
            operator_node.back_node = data_node
            data_node = operator_node
        self.root_node = data_node

if __name__ == '__main__':
    cal = Calculator()