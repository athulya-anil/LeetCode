-- Last updated: 24/08/2026, 12:47:05
# Write your MySQL query statement below
with friends_cte as(
    select user1_id as friends
    from Friendship
    where user2_id = 1
    UNION 
    select user2_id as friends
    from Friendship
    where user1_id = 1
),
friends_recommendation as(
    select page_id
    from friends_cte f join Likes l on l.user_id = f.friends
)

select distinct page_id as recommended_page from Likes where page_id not in (select page_id from Likes where user_id = 1)
and page_id in (select * from friends_recommendation)