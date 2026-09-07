# 步驟1: 取得使用者輸入的已加密文字
encrypted_text = input("請輸入已加密的文字: ")

# 步驟2: 取得使用者輸入的位移值
shift_value = int(input("請輸入位移值: "))

# 步驟3: 解密過程，將每個字節進行反向位移
decrypted_text = ""
for byte in encrypted_text.encode('utf-8'):
    # 逆向位移
    decrypted_byte = (byte - shift_value) % 256
    decrypted_text += chr(decrypted_byte)

# 步驟4: 輸出解密後的文字
print("解密後的文字:", decrypted_text)