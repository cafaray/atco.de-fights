/*
In my solution, I create this dynamic query:
    SELECT MAX(ELT(job = "Job1", name)) `job1`, MAX(ELT(job = "job2", name)) `job2`, ...
    FROM (
            SELECT *, @i:=IF(@j <=> @j:=job, @i+1, 1) line
            FROM employees
            ORDER BY 3, 1
         ) sub_query
    GROUP BY i
- FOR EXAMPLE:
    ┌───┬──────────────────┬─────────────────┐
    │id │       name       │       job       │
    ├───┼──────────────────┼─────────────────┤
    │1  │Grazyna Wawrzyniak│Software Engineer│
    │2  │Maragret Jinks    │Accountant       │
    │3  │Sierra Frakes     │CEO              │
    │4  │Vicenta Mirabella │Software Engineer│
    └───┴──────────────────┴─────────────────┘
- Step 1, I use sub_query, because I want it look like:
    ┌───┬──────────────────┬─────────────────┬──────────┐
    │id │       name       │       job       │   line   │
    ├───┼──────────────────┼─────────────────┼──────────┤
    │2	│Maragret Jinks    │Accountant       │     1    │
    │3	│Sierra Frakes     │CEO              │     1    │
    │1	│Grazyna Wawrzyniak│Software Engineer│     1    │
    │4	│Vicenta Mirabella │Software Engineer│     2    │
    └───┴──────────────────┴─────────────────┴──────────┘
    How it works?

        SELECT *, @i:=IF(@j <=> @j:=job, @i+1, 1) line
        FROM employees
        ORDER BY 3, 1

    I order it by `job`. For each row, if `job` is changing, reset @i = 1, or else set @i = @i + 1
         @i:=IF(@j <=> @j:=job, @i+1, 1) means @i = if(@j == (@j:=job)) then (@i + 1) else 1;

- Step 2, I use ELT function to set value is `name` if it is in the corresponding job, or else set it is NULL
    This function returns the string at the index number specified in the list of arguments.
    ELT(index base 1,str1,str2,...)
    Example: ELT(job = "Accountant", name).
             If job = "Accountant", index is 1, then return `name`,
             else index is 0, this index doesn't exist then return NULL
    
    SELECT ELT(job = "Accountant", name) `Accountant`, 
           ELT(job = "CEO", name)) `CEO`,
           ELT(job = "Software Engineer", name)) `Software Engineer`
    FROM sub_query;

    (The `line` column is not show in this query)
            ┌──────────────────┬──────────────────┬────────────────────┐
     line   │Accountant        │       CEO        │  Software Engineer │
    --------├──────────────────┼──────────────────┼────────────────────┤
       1    │Maragret Jinks    │NULL              │NULL                │
       1    │NULL              │Sierra Frakes     │NULL                │
       1    │NULL              │NULL              │Grazyna Wawrzyniak  │
       2    │NULL              │NULL              │Vicenta Mirabella   │ 
    --------└──────────────────┴──────────────────┴────────────────────┘
- Step 3, Here I come across the problem, the names are not in the same row, how to remove all NULL values?
    It's time to use the `line` column. I will group it by `line` column.
    Each group have only one `name`, the rest are NULL values.
    So I use MAX function to get this name in each group:

        SELECT MAX(ELT(job = "Accountant", name)) `Accountant`, 
               MAX(ELT(job = "CEO", name)) `CEO`,
               MAX(ELT(job = "Software Engineer", name)) `Software Engineer`
        FROM sub_query
        GROUP BY line;

    Now, I have this table:
            ┌──────────────────┬──────────────────┬────────────────────┐
     line   │Accountant        │       CEO        │  Software Engineer │
    --------├──────────────────┼──────────────────┼────────────────────┤
       1    │Maragret Jinks    │Sierra Frakes     │Grazyna Wawrzyniak  │
       2    │NULL              │NULL              │Vicenta Mirabella   │ 
    --------└──────────────────┴──────────────────┴────────────────────┘
*/

/* 270 char
CREATE PROCEDURE employeeList()
BEGIN
    SET group_concat_max_len = 2018,
        @q = (SELECT CONCAT('SELECT ',
                             GROUP_CONCAT(DISTINCT 'MAX(ELT(job = "',job,'",name))`',job,'`'),
                             'FROM (SELECT *, @i:=IF(@j <=> @j:=job, @i+1, 1)_
                                    FROM employees
                                    ORDER BY 3, 1)_
                             GROUP BY _')
              FROM employees);
    PREPARE s from @q;
    EXECUTE s;
END
*/

/* 245 char
CREATE PROCEDURE employeeList()
BEGIN
    SELECT CONCAT('SELECT ',
                   GROUP_CONCAT(DISTINCT 'MAX(ELT(job="',job,'",n))`',job,'`'),
                  'FROM (SELECT *, name n, @i:=IF(@j <=> @j:=job, @i+1, 1)_
                         FROM employees
                         ORDER BY 3, 1)_
                   GROUP BY _') into @q
    FROM employees;
    PREPARE s from @q;
    EXECUTE s;
END
*/

CREATE PROCEDURE employeeList()
BEGIN
    SELECT REPLACE(CONCAT('S	L	CT ', GROUP_CONCAT(DISTINCT 'MAX(	LT(job="',job,'",	))`',job,'`'), 'FROM (S	L	CT *,nam	 	, @	:=IF(@		 <=> @		:=job, @	+1, 1)		 FROM 	mploy		s ORD	R BY 3, 1)	 GROUP BY 		'),'	','e') into @q
    FROM employees;
    PREPARE s from @q;
    EXECUTE s;
END