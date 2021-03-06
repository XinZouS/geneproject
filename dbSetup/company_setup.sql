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

-- == insert the MSSubCat table == -- 
-- INSERT INTO blog_mssubadvs (Name)
-- select MSSubAdv from blog_company 
-- where MSSubAdv is not null 
-- group by MSSubAdv 
-- order by MSSubAdv

-- == insert the MrgName table == -- 
-- INSERT INTO blog_mgrnames (Name)
-- select MgrName from blog_company 
-- where MgrName is not null 
-- group by MgrName 
-- order by MgrName


-- select * from blog_advisors -- count: 1597
-- select * from blog_mscats -- count: 123
-- select * from blog_mssubadvs -- count: 1289
-- select * from blog_mgrnames


-- == test combo search Adv&Cat == --
-- select Advisorid_id, Advisor, mscatdbid_id, mSCat from blog_company
-- where advisorid_id = 12 and mscatdbid_id in (9, 64)
-- order by Advisor 

-- == test combo search Adv&Cat&Sub == --
-- select name, advisorId_id, advisor, mscatdbId_id, mscat, mssubadvId_id, mssubadv from blog_company
-- where advisor is not null and mscat is not null and mssubadv is not null
-- order by advisorid_id


