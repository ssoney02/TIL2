-- yyyy-mm-dd hh:mm:ss 형태로 주어질 때 연도만 뽑아내서 그룹화
SELECT strftime('%Y', "InvoiceDate") AS Year, sum("Total") AS 'TotalSales' FROM invoices
GROUP BY Year;
