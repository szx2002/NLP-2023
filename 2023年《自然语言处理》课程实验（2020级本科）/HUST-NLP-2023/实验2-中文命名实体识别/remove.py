def remove_empty_lines(input_file, output_file):
    with open(input_file, 'r', encoding='ansi') as file:
        lines = file.readlines()

    # 去除空行并生成新的内容列表
    non_empty_lines = [line for line in lines if line.strip()]

    with open(output_file, 'w', encoding='ansi') as file:
        file.writelines(non_empty_lines)


# 示例用法
input_file = 'output1.txt'      # 输入文件路径
output_file = 'output.txt'    # 输出文件路径

remove_empty_lines(input_file, output_file)
