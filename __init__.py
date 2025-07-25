import sys
import os
import importlib
import shutil
import time




WEB_DIRECTORY = os.path.join(os.path.dirname(__file__), "web")
print(WEB_DIRECTORY)
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

def load_all_nodes(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.py') and filename != '__init__.py':
                module_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(module_path, root_dir)
                module_name = rel_path[:-3].replace(os.sep, '.')
                print(f"[DaShuai] 尝试加载模块: {module_name} 从路径: {module_path}")
                try:
                    spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    if hasattr(module, "NODE_CLASS_MAPPINGS"):
                        NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
                        print(f"[DaShuai] 成功加载节点映射: {module.NODE_CLASS_MAPPINGS}")
                    if hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS"):
                        NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)
                except Exception as e:
                    print(f"[DaShuai] 加载模块 {module_name} 失败: {e}")

load_all_nodes(os.path.dirname(__file__))


__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']

