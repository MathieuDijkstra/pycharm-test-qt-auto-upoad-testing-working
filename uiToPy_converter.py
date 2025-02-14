# uitoPy_converter.py
import os
from qtpy import uic


def uiToPy_converter(ui_dir):
    files = os.listdir(ui_dir)
    ui_files = [f for f in files if f.endswith('.ui')]

    for ui_file in ui_files:
        py_file = os.path.splitext(ui_file)[0] + ".py"
        ui_path = os.path.join(ui_dir, ui_file)
        py_path = os.path.join(ui_dir, py_file)

        # Check if the .py file exists
        if not os.path.exists(py_path):
            print(f"'{ui_file}' niet gevonden als '{py_file}', converteren...")
            with open(py_path, 'w') as py_file_handle:
                uic.compileUi(ui_path, py_file_handle)
            print(f"'{ui_file}' is geconverteerd naar '{py_file}'")
        else:
            # Compare modification times of .ui and .py files
            ui_mtime = os.path.getmtime(ui_path)
            py_mtime = os.path.getmtime(py_path)

            if ui_mtime > py_mtime:
                print(f"'{ui_file}' is aangepast na de laatste conversie, converteren opnieuw...")
                with open(py_path, 'w') as py_file_handle:
                    uic.compileUi(ui_path, py_file_handle)
                print(f"'{ui_file}' is opnieuw geconverteerd naar '{py_file}'")
            else:
                print(f"'{ui_file}' is al up-to-date als '{py_file}'.")
