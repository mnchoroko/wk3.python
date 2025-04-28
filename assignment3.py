# File Read & Write Challenge
def read_and_write_file(input_filename, output_filename):
    try:
        # Read the content of the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to {output_filename}.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read or write to the file.")

# Error Handling Lab
def main():
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write the modified content: ")

    # Call the function to read and write the file
    read_and_write_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
