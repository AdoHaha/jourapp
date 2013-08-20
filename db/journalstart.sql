BEGIN TRANSACTION;
CREATE TABLE journal(id integer PRIMARY KEY autoincrement, addeddate text not null, allwords text, noofwords integer, userid integer);
COMMIT;
