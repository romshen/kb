# How to:

Given two tables:
```shell
                         Table "public.people"
 Column |  Type   | Collation | Nullable |           Default            
--------+---------+-----------+----------+------------------------------
 id     | integer |           | not null | generated always as identity
 added  | date    |           | not null | CURRENT_DATE
Indexes:
    "people_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "people_info" CONSTRAINT "people_info_people_id_fkey" FOREIGN KEY (people_id) REFERENCES people(id) ON DELETE CASCADE


                             Table "public.people_info"
  Column   |       Type        | Collation | Nullable |           Default            
-----------+-------------------+-----------+----------+------------------------------
 id        | integer           |           | not null | generated always as identity
 people_id | integer           |           |          | 
 name      | character varying |           |          | 
 phone     | character varying |           |          | 
Foreign-key constraints:
    "people_info_people_id_fkey" FOREIGN KEY (people_id) REFERENCES people(id) ON DELETE CASCADE
```
get data from joined tables by field which contains yesterday date:
```sql
select * from people
inner join people_info on people.id = people_info.people_id where added = current_date - 1;
```