def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                break

    print("Process No. Process Size Block No")
    for i in range(n):
        print(" ", i + 1, "     ", processSize[i], "      ", end="   ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1 or blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j

        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] -= processSize[i]

    print("Process No. Process Size Block No")
    for i in range(n):
        print(" ", i + 1, "     ", processSize[i], "      ", end="   ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

def main():
    blockSize = [100, 500, 200, 300, 600]  
    processSize = [80, 200, 112, 345] 
    m = len(blockSize)
    n = len(processSize)

    while True:
        print("\nMemory Allocation Strategies")
        print("1. First Fit")
        print("2. Best Fit")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            firstFit(blockSize.copy(), m, processSize, n)
        elif choice == '2':
            bestFit(blockSize.copy(), m, processSize, n)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()

