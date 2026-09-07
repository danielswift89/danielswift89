# 步驟1: 取得使用者輸入的已加密文字
encrypted_text = input("請輸入已加密的文字: ")

# 步驟2: 取得使用者輸入的位移值
shift_value = int(input("請輸入位移值: "))

# 步驟3: 解密過程，將每個字符進行反向位移
decrypted_text = ""
for char in encrypted_text:
    # 使用ord取得字符的Unicode碼，加上位移值得到解密後的Unicode碼，再使用chr轉換回字符
    decrypted_char = chr(ord(char) - shift_value)
    decrypted_text += decrypted_char

# 步驟4: 輸出解密後的文字
print("解密後的文字:", decrypted_text)
