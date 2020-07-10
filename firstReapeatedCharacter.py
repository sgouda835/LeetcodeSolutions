# def firstRepeatedChar(str):
#     # dict ={}
#     #
#     # for ch in str:
#     #     if ch in dict:
#     #         return ch
#     #     else:
#     #         dict[ch] = 0
#     # return None
#     #
#
#     repeating = ""
#
#     charSet = set()
#     for c in str:
#         if c.isalpha():
#             if c in charSet:
#                 repeating = c
#                 break
#             else:
#                 charSet.add(c)
# print(f"First repeating char: {repeating}")
# print(firstRepeatedChar("geeksforgeeks"))
text = "geeksforgeeks"
print(f"text: {text}")

repeating = ""

charSet = set()
for c in text:
    if c.isalpha():
        if c in charSet:
            repeating = c
            break
        else:
            charSet.add(c)

print(f"First repeating char: {repeating}")