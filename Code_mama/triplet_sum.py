def find_triplet(arr, N, P):
    arr.sort()

    for i in range(N - 2):  
        left = i + 1
        right = N - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == P:               
                print(f"{arr[i]} {arr[left]} {arr[right]}")
                return
            elif current_sum < P:
                left += 1
            else:
                right -= 1
   
    print("No triplet found")

if __name__ == "__main__":   
    N = int(input())
    if N < 3:
        print("No triplet found")
    else:
        arr = list(map(int, input().split()))
        P = int(input())
        
        find_triplet(arr, N, P)