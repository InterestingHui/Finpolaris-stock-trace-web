#!/usr/bin/env python3
"""
替换前端 HTML 中的 __BACKEND_URL__ 占位符为环境变量 BACKEND_URL 的值。
用法：
    python replace_backend_url.py <html文件路径>
如果未指定文件路径，默认处理当前目录下的 index.html。
环境变量 BACKEND_URL 未设置时，替换为空字符串。
"""

import os
import sys

def replace_placeholder(file_path, placeholder="__BACKEND_URL__"):
    # 读取环境变量，若不存在则设为空字符串
    backend_url = os.environ.get("BASE_URL", "")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        sys.exit(1)

    # 替换占位符
    new_content = content.replace(placeholder, backend_url)

    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"已将 {placeholder} 替换为 '{backend_url}'，文件已更新：{file_path}")

if __name__ == "__main__":
    # 获取目标文件路径，默认 index.html
    target_file = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    replace_placeholder(target_file)