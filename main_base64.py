import base64


def decode_multiple_base64(input_file="base.txt", output_prefix="base64_output"):
    try:
        with open(input_file, "r") as file:
            lines = file.readlines()

        count = 1

        for line in lines:
            base64_str = line.strip()

            if not base64_str:
                continue  # skip empty lines

            try:
                # Remove any internal whitespace
                base64_clean = "".join(base64_str.split())

                # Decode
                decoded_bytes = base64.b64decode(base64_clean)

                # Try decoding as UTF-8 text
                try:
                    decoded_text = decoded_bytes.decode("utf-8")
                    out_filename = f"{output_prefix}_{count}.txt"

                    with open(out_filename, "w", encoding="utf-8") as out_file:
                        out_file.write(decoded_text)
                    print(f"[Text] Decoded to {out_filename}")

                except UnicodeDecodeError:
                    # Binary output fallback
                    out_filename = f"{output_prefix}_{count}.bin"

                    with open(out_filename, "wb") as out_file:
                        out_file.write(decoded_bytes)
                    print(f"[Binary] Decoded to {out_filename}")

                count += 1

            except Exception as decode_error:
                print(f"Error decoding line {count}: {decode_error}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    decode_multiple_base64()


if __name__ == "__main__":
    main()
