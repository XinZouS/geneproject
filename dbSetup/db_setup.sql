-- select Advisor, min(inceptdt) from company group by advisor -- as Advisors

-- select * from blog_company

-- select mscat, mscatid from blog_company
-- where advisorid_id IN (177, 282, 173) order by name


-- == insert the Advisor table == -- 
-- insert into blog_advisors (Name)
-- select Advisor from blog_company 
-- where Advisor IS NOT  NULL
-- group by Advisor 
-- order by Advisor

-- == insert the MSCat table == -- 
-- INSERT INTO blog_mscats (Name)
-- select mscat from blog_company
-- where mscat IS NOT NULL
-- group by mscat
-- order by mscat


-- select * from blog_mscats
-- select * from blog_advisors

-- select Advisorid_id, Advisor, mscatdbid_id, mSCat from blog_company
-- where advisorid_id = 12 and mscatdbid_id in (9, 64)
-- order by Advisor 
