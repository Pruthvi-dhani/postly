BEGIN;
--
-- Add field is_deleted to commentlikes
--
ALTER TABLE "likes_commentlikes" ADD COLUMN "is_deleted" boolean DEFAULT false NOT NULL;
ALTER TABLE "likes_commentlikes" ALTER COLUMN "is_deleted" DROP DEFAULT;
--
-- Add field is_deleted to postlikes
--
ALTER TABLE "likes_postlikes" ADD COLUMN "is_deleted" boolean DEFAULT false NOT NULL;
ALTER TABLE "likes_postlikes" ALTER COLUMN "is_deleted" DROP DEFAULT;
COMMIT;
