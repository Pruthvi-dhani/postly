BEGIN;
CREATE TABLE "user_user" (
"id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
"username" varchar(50) NOT NULL,
"email" varchar(256) NOT NULL,
"about" varchar(1024) NOT NULL,
"password" varchar(256) NOT NULL,
"is_deleted" boolean NOT NULL);
COMMIT;

BEGIN;
ALTER TABLE "user_user"
ALTER COLUMN is_deleted
SET DEFAULT false;
COMMIT;