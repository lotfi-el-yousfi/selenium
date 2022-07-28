import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = 1;

excel.Workbooks.Open('G:/working.xlsx')

XlDirectionDown = 4

last = excel.Range("A:A").End(XlDirectionDown)
excel.Range("A1:A"+str(last)).Select()