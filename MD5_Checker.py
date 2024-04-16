import sys
import hashlib
import os

def calculate_md5(file_name):
    try:
        if not os.path.isfile(file_name):
            raise FileNotFoundError("The file does not exist.")
        
        hash_md5 = hashlib.md5()
        with open(file_name, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    except PermissionError:
        print("Permission denied to read the file.")
        sys.exit(1)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python md5_checker.py  []")
        sys.exit(1)

    file_name = sys.argv[1]
    if len(file_name) > 256:
        print("Filename too long. Please provide a valid filename.")
        sys.exit(1)

    md5_hash = calculate_md5(file_name)

    if len(sys.argv) == 3:
        user_hash = sys.argv[2]
        if len(user_hash) != 32:
            print("Invalid hash length. MD5 hash should be 32 characters long.")
            sys.exit(1)
        if md5_hash == user_hash:
            print("Authenticated")
        else:
            print("Failed to Match!")

    print(f"File's MD5 Hash: {md5_hash}")

if __name__ == "__main__":
    main()