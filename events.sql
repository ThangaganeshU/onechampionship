CREATE TABLE events (
  id int, 
  event_name varchar(10), 
  people_count int
);

/************************************/

Insert into events 
values 
  (1, 'ABC1', 10);
Insert into events 
values 
  (2, 'ABC2', 109);
Insert into events 
values 
  (3, 'ABC3', 150);
Insert into events 
values 
  (4, 'ABC4', 99);
Insert into events 
values 
  (5, 'ABC6', 145);
Insert into events 
values 
  (6, 'ABC7', 1455);
Insert into events 
values 
  (7, 'ABC8', 199);
Insert into events 
values 
  (8, 'ABC9', 188);
Insert into events 
values 
  (9, 'ABC10', 188);
Insert into events 
values 
  (10, 'ABC11', 10);
Insert into events 
values 
  (11, 'ABC12', 100);
Insert into events 
values 
  (12, 'ABC13', 100);
Insert into events 
values 
  (13, 'ABC14', 100);



/************************************/

SELECT
   COUNT_OCCUR_QRY.ID,
   COUNT_OCCUR_QRY.EVENT_NAME,
   COUNT_OCCUR_QRY.PEOPLE_COUNT 
FROM
   (
      SELECT
         CONSEC_QRY.*,
         Count(*)OVER(PARTITION BY CONSEC_QRY.CONSEC_GRP) CNTS 
      FROM
         (
            SELECT
               ID,
               EVENT_NAME,
               PEOPLE_COUNT,
               ROW_NUMBER() OVER (
            ORDER BY
               ID) ROW_NM,
               ID - ROW_NUMBER() OVER (
            ORDER BY
               ID) CONSEC_GRP 
            FROM
               EVENTS 
            WHERE
               PEOPLE_COUNT >= 100 
         )
         CONSEC_QRY 
   )
   COUNT_OCCUR_QRY 
ORDER BY
   COUNT_OCCUR_QRY.ID 
WHERE
   COUNT_OCCUR_QRY.CNTS >= 3 ;

/************************************/
