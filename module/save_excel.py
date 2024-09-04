"""
전달받은 개인정보 리스트를 엑셀에 저장합니다
"""

import os
import openpyxl


def save_infos_to_excel(infos, excel_file):
    """개인정보를 찾은 리스트를 엑셀 파일로 저장합니다."""
    if os.path.exists(excel_file):
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active
    else:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["연번", "파일명", "페이지번호", "유형", "내용"])
    start_no = sheet.max_row if sheet.cell(
        row=1, column=1).value == "No." else 0

    for i, info in enumerate(infos, start=start_no + 1):
        sheet.append([i] + list(info))

    workbook.save(excel_file)
