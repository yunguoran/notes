import openpyxl
import re

def xlsx_to_compact_markdown_table(xlsx_path, sheet_name):
    wb = openpyxl.load_workbook(xlsx_path)
    sheet = wb[sheet_name]
    rows = list(sheet.iter_rows(values_only=True))

    if not rows:
        return ""

    header = rows[0]  # 表头
    data = rows[1:]   # 数据

    # ✅ 按照第一列升序排序，忽略 None 值
    data = sorted(data, key=lambda x: (x[0] is None, str(x[0]).lower()))

    # ✅ 生成 Markdown 表格
    header_line = "| " + " | ".join(str(h) for h in header) + " |"
    separator_line = "| " + " | ".join([":---" for _ in header]) + " |"
    lines = [header_line, separator_line]

    for row in data:
        row_line = "| " + " | ".join("" if cell is None else str(cell) for cell in row) + " |"
        lines.append(row_line)

    return "\n".join(lines)

def replace_section_in_md(md_path, section_title, new_table):
    with open(md_path, encoding='utf-8') as f:
        content = f.read()

    # ✅ 精准匹配段落，只保留段落下一行空行
    pattern = rf"(## {re.escape(section_title)}\n)(.*?)(?=\n## |\Z)"
    replacement = rf"\1\n{new_table}\n"

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count == 0:
        print(f"❌ 未找到 ## {section_title} 段落，请检查拼写/格式")
    else:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ 成功替换 ## {section_title} 段内容，且格式紧凑规范")

# === 执行 ===
xlsx_file = "english/phrases.xlsx"
md_file = "english/english.md"

word_table = xlsx_to_compact_markdown_table(xlsx_file, sheet_name="word")
replace_section_in_md(md_file, "Word", word_table)

phrase_table = xlsx_to_compact_markdown_table(xlsx_file, sheet_name="phrase")
replace_section_in_md(md_file, "Phrase", phrase_table)
