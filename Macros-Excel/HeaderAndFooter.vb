
'website:
'https://docs.microsoft.com/en-us/office/vba/excel/concepts/workbooks-and-worksheets/formatting-and-vba-codes-for-headers-and-footers

Sub CenterFooter()

txt = Range("A392").Value
 ActiveSheet.PageSetup.CenterFooter = txt & Chr(10) & "&P of &N"
End Sub
