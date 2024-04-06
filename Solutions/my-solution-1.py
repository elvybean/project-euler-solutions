# to solve implement algorithm similar to fizz-buzz but instead of 
# printing numbers add multiples of 3 or 5 to integer that is a running total

def main():
    total = 0
    for i in range(0, 1000):
        i += 1
        match [i % 3 == 0, i % 5 == 0]:
            case [False, False]:
                total += 0
            case other:
                total += i
    print("sum of all the multiples of 3 or 5 below 1000 is:", total,)
                
if __name__ == "__main__":
    main()