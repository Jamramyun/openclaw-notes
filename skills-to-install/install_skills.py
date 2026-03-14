#!/usr/bin/env python3
"""
自动安装技能ZIP包
放在 skills-to-install 目录的ZIP文件会被自动解压安装
"""

import os
import zipfile
import json
import shutil

SKILLS_DIR = "/root/.openclaw/workspace/skills-to-install"
INSTALL_TARGET = "/root/.openclaw/workspace/skills"

def install_skill_zip(zip_path):
    """安装单个技能ZIP包"""
    skill_name = os.path.basename(zip_path).replace('.zip', '')
    extract_path = os.path.join(SKILLS_DIR, skill_name)
    
    print(f"\n📦 安装: {skill_name}")
    
    try:
        # 解压
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"  ✅ 解压完成")
        
        # 检查是否是有效技能包
        package_json = os.path.join(extract_path, 'package.json')
        skill_json = os.path.join(extract_path, 'skill.json')
        
        if os.path.exists(package_json) or os.path.exists(skill_json):
            # 移动到正式技能目录
            final_path = os.path.join(INSTALL_TARGET, skill_name)
            if os.path.exists(final_path):
                shutil.rmtree(final_path)
            shutil.move(extract_path, final_path)
            print(f"  ✅ 安装到: {final_path}")
            return True
        else:
            print(f"  ⚠️  不是有效技能包，保留在临时目录")
            return False
            
    except Exception as e:
        print(f"  ❌ 安装失败: {e}")
        return False

def main():
    print("=" * 50)
    print("技能安装工具")
    print("=" * 50)
    
    # 确保目标目录存在
    os.makedirs(INSTALL_TARGET, exist_ok=True)
    
    # 查找所有ZIP文件
    zip_files = [f for f in os.listdir(SKILLS_DIR) if f.endswith('.zip')]
    
    if not zip_files:
        print("\n没有找到ZIP文件")
        print(f"请将技能ZIP包放到: {SKILLS_DIR}")
        return
    
    print(f"\n发现 {len(zip_files)} 个技能包:")
    for i, zip_file in enumerate(zip_files, 1):
        print(f"  {i}. {zip_file}")
    
    # 逐个安装
    success_count = 0
    for zip_file in zip_files:
        zip_path = os.path.join(SKILLS_DIR, zip_file)
        if install_skill_zip(zip_path):
            success_count += 1
            # 安装成功后删除ZIP
            os.remove(zip_path)
            print(f"  🗑️  已删除ZIP文件")
    
    print(f"\n✅ 安装完成: {success_count}/{len(zip_files)}")
    print(f"\n已安装技能:")
    if os.path.exists(INSTALL_TARGET):
        for skill in os.listdir(INSTALL_TARGET):
            if os.path.isdir(os.path.join(INSTALL_TARGET, skill)):
                print(f"  - {skill}")

if __name__ == '__main__':
    main()
