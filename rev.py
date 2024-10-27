def make(input_str):
    # Step 1: Reverse the input string
    reversed_str = input_str[::-1]
    
    # Step 2: Add "abc" at the beginning and end
    addabc = "abc" + reversed_str 
    addabc = addabc+"abc"
    
    # Step 3: Remove characters at index 0 and last index
    remove0= addabc[1:-1]
    
    # Step 4: Reverse the string again
    rev2 = remove0[::-1]
    
    # Step 5: Remove the first two and last two characters
    remove12= rev2[2:-2]
    
    # Step 6: Reverse the string once more
    finaloutput= remove12[::-1]
    
    return finaloutput

# Example usage
input_string = "AJVaHREGgf5Xfs"
result = make(input_string)
print(result)