def is_valid_binary(input_string):
    S = {"00", "10", "010", "01001"}
    n = len(input_string)
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for pattern in S:
            if i >= len(pattern) and dp[i - len(pattern)] and input_string[i - len(pattern):i] == pattern:
                dp[i] = True
                break 
    
    if dp[n]:
        print("Valid")
    else:
        print("Tidak Valid")
        
if __name__ == "__main__":
    input_string = input("Input binary: ")
    is_valid_binary(input_string)