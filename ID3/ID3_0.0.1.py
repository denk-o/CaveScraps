from numpy import exp, array, random, dot
#not sure if we need all these but yolo

class ID3():
    def __init__(self):
        self.rows = 0
        self.cols = 0
    def readFile(self, fileName):
        f = open(fileName, 'r')
        arr = f.readline().split(' ')
        self.rows = arr[0]
        self.cols = arr[1]
        print(self.rows)
        print(self.cols)
if __name__ == "__main__":
    I = ID3()
    I.readFile('input.txt')
