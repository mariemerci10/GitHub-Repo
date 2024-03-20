def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1.\n")
            file.write("12345\n")
            file.write("Another line here with some numbers: 98765\n")
        print("File 'my_file.txt' created successfully.")
    except Exception as e:
        print(f"Error occurred while creating file: {e}")
    finally:
        file.close()

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of 'my_file.txt':")
            print(file.read())
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to read 'my_file.txt'.")
    except Exception as e:
        print(f"Error occurred while reading file: {e}")
    finally:
        file.close()

def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1.\n")
            file.write("Appending line 2.\n")
            file.write("Appending line 3.\n")
        print("Lines appended to 'my_file.txt' successfully.")
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to append 'my_file.txt'.")
    except Exception as e:
        print(f"Error occurred while appending file: {e}")
    finally:
        file.close()

if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
