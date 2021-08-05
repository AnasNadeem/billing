import os
import webbrowser
cwd = f'{os.getcwd()}'
pdf_p = 'anas_400_08-04-21.pdf'
fol_path = os.path.join(cwd, 'bill_invoice')
full_path = os.path.join(fol_path, pdf_p)
webbrowser.open_new(f'file://{full_path}')
# os.system(full_path)
