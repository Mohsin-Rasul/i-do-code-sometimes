import os
import hashlib
import getpass
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 16
CHUNK_SIZE = 64 * 1024


def derive_key(password):
    return hashlib.sha256(password.encode("utf-8")).digest()


def pad(data):
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len]) * pad_len


def unpad(data):
    if not data:
        return data
    pad_len = data[-1]
    if pad_len < 1 or pad_len > BLOCK_SIZE:
        raise ValueError("Invalid padding")
    return data[:-pad_len]


def encrypt_file(filename, password):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    key = derive_key(password)
    iv = get_random_bytes(BLOCK_SIZE)
    output_name = f"(enc){os.path.basename(filename)}"

    with open(filename, "rb") as infile, open(output_name, "wb") as outfile:
        outfile.write(os.path.getsize(filename).to_bytes(8, "big"))
        outfile.write(iv)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        previous_chunk = infile.read(CHUNK_SIZE)
        if not previous_chunk:
            outfile.write(cipher.encrypt(pad(b"")))
            return output_name

        while True:
            current_chunk = infile.read(CHUNK_SIZE)
            if not current_chunk:
                if len(previous_chunk) % BLOCK_SIZE != 0:
                    previous_chunk = pad(previous_chunk)
                else:
                    previous_chunk += bytes([BLOCK_SIZE]) * BLOCK_SIZE
                outfile.write(cipher.encrypt(previous_chunk))
                break
            outfile.write(cipher.encrypt(previous_chunk))
            previous_chunk = current_chunk

    return output_name


def decrypt_file(filename, password):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    with open(filename, "rb") as infile:
        original_size = int.from_bytes(infile.read(8), "big")
        iv = infile.read(BLOCK_SIZE)
        if len(iv) != BLOCK_SIZE:
            raise ValueError("Encrypted file is corrupted or incomplete")

        key = derive_key(password)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        output_name = os.path.basename(filename)
        if output_name.startswith("(enc)"):
            output_name = output_name[len("(enc)"):]

        with open(output_name, "wb") as outfile:
            while True:
                chunk = infile.read(CHUNK_SIZE)
                if not chunk:
                    break
                if len(chunk) % BLOCK_SIZE != 0:
                    raise ValueError("Encrypted file is corrupted or not a valid AES file")
                outfile.write(cipher.decrypt(chunk))
            outfile.truncate(original_size)

    return output_name


def main():
    print("AES-CBC File Encryptor")
    action = input("Type E to encrypt or D to decrypt: ").strip().upper()
    filename = input("Enter filename: ").strip()
    password = getpass.getpass("Enter password: ")

    if action == "E":
        output = encrypt_file(filename, password)
        print(f"Encrypted file saved as: {output}")
    elif action == "D":
        output = decrypt_file(filename, password)
        print(f"Decrypted file saved as: {output}")
    else:
        print("Invalid option. Use E or D.")


if __name__ == "__main__":
    main()


