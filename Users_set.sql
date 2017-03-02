SELECT * FROM user;

COMMIT;

UPDATE mysql.user
   SET Host = 'c1246895-xps.home'
 WHERE Host LIKE '192.168.1.20';