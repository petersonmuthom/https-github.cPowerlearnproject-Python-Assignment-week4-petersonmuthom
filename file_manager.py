# Combined File Read & Write Challenge with Error Handling
try:
  
    input_filename = input("Enter the filename to read: ")

   
    with open(input_filename, "r") as input_file:
        content = input_file.read()

    
    modified_content = content.upper()

 
    output_filename = input("Enter the filename to write the modified content to: ")

 
    with open(output_filename, "w") as output_file:
        output_file.write(modified_content)

    print(f"File processed successfully. Modified content written to '{output_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied for file '{input_filename}' or '{output_filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
