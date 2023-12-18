import random
class JapaneseEncoderDecoder:
    def generate_random_key(word_len):
        # Generate a list of random numbers for encoding
        return [random.randint(1, 9) for _ in range(word_len)]

    @staticmethod
    def encode(encode_input):
        def divide_value(value, divisor):
            part1 = value // divisor
            part2 = value - part1
            return part1, part2
        answer = ""
        length = len(encode_input)
        char_list = list(encode_input)
        print(char_list)
        unique_key = JapaneseEncoderDecoder.generate_random_key(length)

        for char, key in zip(char_list, unique_key):
            converted_char = format(ord(char), '#08x')
            num = int(converted_char, 16)
            seom = (divide_value(num, key))
            answer += (chr(int(seom[0])))
            answer += (chr(int(seom[1])))
        print("Key (Copy to remember): ", unique_key)
        return answer

    @staticmethod
    def decode(decode_input):
        result = ""
        for i in range(0, len(decode_input), 2):
            char_pair = decode_input[i:i + 2]

            char1 = char_pair[0]
            char2 = char_pair[1]

            hex1 = format(ord(char1), '#08x')
            hex2 = format(ord(char2), '#08x')

            sum_res = (int(hex1, 16) + int(hex2, 16))
            result += (chr(int(sum_res)))
        return result


def main():
    encoder_decoder = JapaneseEncoderDecoder()

    while True:
        print("Choose an option:")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("Enter your choice, (1 ~ 3): ")

        if choice == '1':
            encode_input = input("Enter string to encode: ")
            encoded_result = encoder_decoder.encode(encode_input)
            print(f"Encoded result: {encoded_result}")
        elif choice == '2':
            decode_input = input("Enter string to decode (Length must be even): ")
            if len(decode_input) % 2 != 0:
                print("Invalid input")
            decoded_result = encoder_decoder.decode(decode_input)
            print(f"Decoded result: {decoded_result}")
        elif choice == '3':
            print("exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
