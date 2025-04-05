BEGIN;
--
-- Alter field password on user
--
ALTER TABLE "user_user" ALTER COLUMN "password" TYPE varchar(60);
COMMIT;