 def get_list_of_squares_of_even_numbers(input_list): 
   return [x**2 for x in input_list if x % 2 == 0]
   def get_sublist(input_list, start_index, end_index):
     return input_list[start_index:end_index] 
     def main(): input_list = list(map(int, input("Enter the list of integers (comma separated): ").split(',')))
       

     squares_of_even_numbers = get_list_of_squares_of_even_numbers(input_list) 
     print(f"List of squares of even numbers: {squares_of_even_numbers}")

    
     start_index = int(input("Enter start index: ")) 
     end_index = int(input("Enter end index: ")) 
     sublist = get_sublist(input_list, start_index, end_index)
     print(f"Sublist: {sublist}")
     if __name__ == "__main__":
       main()
