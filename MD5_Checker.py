import sys
import hashlib

def calculate_md5(file_name):
    hash_md5 = hashlib.md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python MD5_Checker.py  []")
        return

    file_name = sys.argv[1]
    md5_hash = calculate_md5(file_name)

    if len(sys.argv) == 3:
        user_hash = sys.argv[2]
        if md5_hash == user_hash:
            print("Authenticated")
        else:
            print("Failed to Match!")

    print(f"File's MD5 Hash: {md5_hash}")

if __name__ == "__main__":
    main()