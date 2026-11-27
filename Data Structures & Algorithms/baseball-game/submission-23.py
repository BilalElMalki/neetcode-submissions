class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []
        sum = 0

        for i in range(len(operations)):
            if (operations[i] == "D"):
                number = 2 * int(record[len(record) - 1])
                record.append(str(number))

            elif(operations[i] == "C"):
                record.pop()

            elif(operations[i] == "+"):
                record.append(int(record[len(record) - 1]) + int(record[len(record) - 2]))
            else:
                record.append(operations[i])       

        for i in range(len(record)):
            print(record[i])
            sum += int(record[i])  

        return sum        