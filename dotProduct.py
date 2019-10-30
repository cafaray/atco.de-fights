def dotProduct(v1, v2):
    s=0
    for x in zip(v1, v2):
       s+=x[0]*x[1]
    return s


SELECT 
A.cdperson, 
dsrfc, 
dsrazsoc, 
YEAR(dsfecha) AS any, 
COUNT(cddocele) AS documentos, 
SUM(dbtotal) as total,
'MXN' 
  FROM jdem20t A INNER JOIN jpem00t B ON A.cdperson = B.cdperson 
WHERE dsmoneda NOT IN ('1', 'DL', 'Dolar', 'Dólar Americano', 'Dolares', 'Dolares U.S.D.', 'DOLARES US', 'D¢lares','usd') 
GROUP BY cdperson ORDER BY any
INTO OUTFILE 'stats-mxn.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ';'
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';


SELECT 
A.cdperson, 
dsrfc, 
dsrazsoc, 
YEAR(dsfecha) AS any, 
COUNT(cddocele) AS documentos, 
SUM(dbtotal*dbtipcam) as total,
'USD' 
  FROM jdem20t A INNER JOIN jpem00t B ON A.cdperson = B.cdperson 
WHERE dsmoneda IN ('1', 'DL', 'Dolar', 'Dólar Americano', 'Dolares', 'Dolares U.S.D.', 'DOLARES US', 'D¢lares','usd') 
GROUP BY cdperson ORDER BY any
INTO OUTFILE 'stats-usd.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ';'
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';
