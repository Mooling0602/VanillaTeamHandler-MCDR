#!/bin/python
import os
import shutil
import sys


def remove_pycache_dirs(start_dir='.'):
    """
    递归删除指定目录及其子目录中的所有__pycache__文件夹，忽略.venv目录

    Args:
        start_dir (str): 起始目录，默认为当前目录
    """
    removed_count = 0
    for root, dirs, files in os.walk(start_dir, topdown=True):
        # 从遍历列表中移除.venv目录，避免进入
        if '.venv' in dirs:
            dirs.remove('.venv')

        if '.git' in dirs:
            dirs.remove('.git')

        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            try:
                shutil.rmtree(pycache_path)
                print(f"已删除: {pycache_path}")
                removed_count += 1
            except Exception as e:
                print(f"删除失败 {pycache_path}: {e}")

    print(f"\n总共删除了 {removed_count} 个 __pycache__ 文件夹")


if __name__ == "__main__":
    # 如果没有指定目录，则使用当前目录
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'

    print(f"正在扫描目录: {os.path.abspath(target_dir)}")
    confirm = input("确定要删除所有 __pycache__ 文件夹吗？(y/N): ")

    if confirm.lower() == 'y':
        remove_pycache_dirs(target_dir)
    else:
        print("操作已取消")
