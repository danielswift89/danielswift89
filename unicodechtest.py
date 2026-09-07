original_char = '३'
decrypted_char = '香'

# 計算 Unicode 編碼的差值
shift_value = ord(decrypted_char) - ord(original_char)

print("字符移動的位移值:", shift_value)
