# generate Fibonacci list less than 4 million and simultaneously check if the value is even and then add to running total

def fibonacci():
    # note: fibonacci to the 32nd term is greater than 4 million
    a = 1
    b = 2
    fibSeq = [1, 2]
    fibSeqTotal = 0
    for i in range (0, 30):
        c = a + b
        a = b
        b = c

        fibSeqTotal += b
        fibSeq.append(b)

    print(fibSeqTotal)
    print(fibSeq)

def even():
    print()

def main():
    totalEven = 2
    fibSeq = [1, 2]

    for i in range(0, 1000):
        print(i)
        match bool(i > 2):
            case True:
                value = fibSeq[i-2] + fibSeq[i-1]
                print(fibSeq[i-2])
                print(fibSeq[i-1])
                print(value)
                fibSeq.append(value)
                match bool(value % 2 == 0):
                    case True:
                        totalEven += value
    #print("sum of the even-valued terms in the Fibonacci sequence below 4 million is:", totalEven,)
                
if __name__ == "__main__":
    #main()
    fibonacci()