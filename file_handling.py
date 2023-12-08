def copy_file(input_file_path, output_file_path):
  try:
      # Open the input file in read mode
      with open(input_file_path, 'r') as input_file:
          # Read the contents of the input file
          content = input_file.read()

          # Open the output file in write mode
          with open(output_file_path, 'w') as output_file:
              # Write the contents to the output file
              output_file.write(content)

      print(f"File copied successfully from {input_file_path} to {output_file_path}")

  except FileNotFoundError:
      print("Error: One of the files not found.")
  except Exception as e:
      print(f"Error: {e}")

# Example usage:
input_file_path = 'BOB.txt'
output_file_path = 'output.txt'
copy_file(input_file_path, output_file_path)