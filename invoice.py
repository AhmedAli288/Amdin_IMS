import os
import sale_form
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

file_path = 'D:\\ims\\invoice\\'


def print_invoice(bill_ids, items, grand_total):

    DATA = []
    headings = ["Sr. #", "Product", "Qty",
                "Discount", "Price (Rs.)", "Total (Rs.)", ]
    DATA.append(headings)

    for prod in items:
        DATA.append(prod)

    footer = ["", "", "", "Grand Total", grand_total]
    DATA.append(footer)

    bill_id = str(bill_ids)

    # creating a Base Document Template of page size A4
    pdf = SimpleDocTemplate(file_path + bill_id + ".pdf", pagesize=A4)

    # standard stylesheet defined within reportlab itself
    styles = getSampleStyleSheet()

    # fetching the style of Top level heading (Heading1)

    bill_id_style = styles["Heading3"]

    # 0: left, 1: center, 2: right
    bill_id_style.alignment = 0

    # creating the paragraph with
    # the heading text and passing the styles of it
    bill_id_title = Paragraph("Bill ID: " + bill_id, bill_id_style)

    # creates a Table Style object and in it,
    # defines the styles row wise
    # the tuples which look like coordinates
    # are nothing but rows and columns

    val = len(items)

    style = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (6, val), 1, colors.black),
            ("BACKGROUND", (0, 0), (5, 0), colors.gray),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ]
    )

    # creates a table object and passes the style to it
    table = Table(DATA, style=style)

    # final step which builds the
    # actual pdf puting together all the elements
    pdf.build([bill_id_title, table])

    print("invoice working")

    # win32.win32api.ShellExecute(0, "print", file_path, None, ".", 0)
    # os.startfile(file_path + bill_id + ".pdf", 'print')
