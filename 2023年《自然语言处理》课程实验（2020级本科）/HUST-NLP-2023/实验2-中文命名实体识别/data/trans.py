input_file = "ner_test.txt"
output_file = "test_data.txt"

with open(input_file, 'r', encoding='gbk') as f:
    input_text = f.read().strip()

# 将文本拆分为单个字符
characters = list(input_text)

# 将字符序列保存到文件
with open(output_file, 'w', encoding='gbk') as f:
    for char in characters:
        f.write(char + ' 0\n')
