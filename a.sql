BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "title" varchar(250) NOT NULL, 
    "slug" varchar(250) NOT NULL, 
    "body" text NOT NULL, 
    "publish" datetime NOT NULL, 
    "created" datetime NOT NULL, 
    "updated" datetime NOT NULL, 
    "status" varchar(2) NOT NULL, 
    "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
CREATE INDEX "blog_post_publish_bb7600_idx" ON "blog_post" ("publish" DESC);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;


SELECT "blog_post"."id", "blog_post"."title", "blog_post"."slug", "blog_post"."author_id", "blog_post"."body", "blog_post"."publish", "blog_post"."created", "blog_post"."updated", "blog_post"."status" 

FROM "blog_post" 

WHERE "blog_post"."title" = Sinaloa is Great 

ORDER BY "blog_post"."publish" DESC