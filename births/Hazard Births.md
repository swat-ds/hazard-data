# HAZARD BIRTHS

------- 

create new column - column name: sort

```
random()
```

------
## DATE
------

Year - edit column - join columns - Year, Month, Day
> replace nulls with dash (-)

> write result in new column named Date

---- 
## NAMES
----
### Father's Name

Note - edit column - add column based on this column - column name: Father
```
value.split(/&/)[0].replace(/.*dt of |.* s of /,"").replace(/\s{2}.*|,/,'').replace(/\.|;/,"".).trim()
```
Father - edit cells - transform
```
value.replace(/.*[Ss] of/,"")
```
> to remove extraneous symbols before the father's name

Father - edit cells - transform
```
value.replace(/\(.*/,"")
```
> removed the father's dad's name (i.e. Richard (s of Isaac))

Father - edit cells -transform
```
value.replace(/.*w of .*/,"")
```
> removed spouses names that were captured

----
### Mother's Name

Note - edit column - add column based on this column - column name: Mother
```
value.split(/&/)[1].replace(/\s{2}.*|,/,'').replace(/\.|;/,"").trim()
```
Mother - edit cells - transform
```
value.replace(/\(.*/,"")
```
> removed the mothers's mom's name (i.e. Lisa (dt of Elizabeth))

Mother - edit cells - transform
```
value.replace(/,?1st|2nd|2d|3rd|4th/,"").replace(/\s{2}.*|,/,'').trim()
```
> removes 1st, 2nd, and 3rd from the beginning of the mother's name

----
### Spouse's Name

Note - edit column - add column based on this column - column name: Spouse(s)
```
value.split(/([wh] of)/)[1].replace(/\s{2}.*|,/,'').replace(/\.|;/,"").trim()
```
> captures the name after "w or h of..."

Spouse(s) - edit cells - transform
```
value.replace(/ &| and/,";")
```
> separates spouses names with semi-colons

Spouse(s) - edit cells - transform
```
value.replace(/\(.*/,"")
```
> removes dates in parentheses

Spouse(s) - edit cells - transform
```
value.replace(/,?1st|2nd|2d|3rd|4th/,"").trim()
```
> removes 1st, 2nd, and 3rd from the beginning of the spouses' names

Note - text filter - rmt
Spouse(s) - facet - customized facet - facet blank - true
Spouse(s) - edit cells - transform
```
cells.Note.value.split(/rmt /)[1].replace(/\s{2}.*|, .*|; .*/,"")
```
> captures spouses after "rmt"

----
### Sibling's Name

Note - edit column - add column based on this column - column name: Sibling(s)
```
value.split(/[Tt]win of /)[1].replace(/\s{2}.*|,/,'').replace(/\.|;/,"").trim()
```
> captures twins

----
### New Surname

Note - edit column - add column based on this column - column name: New Surname
```
value.split(/ [Nn]ow/)[1].replace(/;|:|\. /,"").replace(/\s{2}.*|,/,'').trim()
```
> captures the name after "now"

---
### Spouses Surname

Spouse - edit column - add column based on this column - column name: Spouses Surname
```
value.split(/\W+/)[-1]
```
> this is only for the purpose of determining column "Not Surname at Birth"

----
### Spouses Surname

Last Name - edit column - join columns - Last Name, Spouse Surname
> replace nulls with space ( )

----
### Surname at Birth?

Not Surname at Birth - edit cells - transform
> write result in new column named Not Surname at Birth
```
filter(value.replace(/\W/," ").ngram(2),n,n.split(" ").uniques().length()!=2).length()>0
```
> returns true if the spouses surname is the same as the last name of their partners

> *explanation:* 
> - combines the columns Last Name and Spouse Surname into the column Not Surname at Birth
> - checks to see if the two names are the same
> - returns true if the names are the same

grandchild/grandson/granddaughter
foster child

-------
## NON-MEMBER
-------

Note - edit column - add column based on this column - column name: Non-Member
```
value.contains(/[Nn]ot a mbr/)
```
> captures non-members

-------
## LOCATION
-------

Note - edit column - add column based on this column - column name: Location
```
value.split(/[A-Z]^\.[A-Z]^\./)[0].split(/  /)[1]
```
> captures  locations

****
Location - facet - customized facet - facet blank - true

```
cells.Note.value.find(/[A-Z].[A-Z]./)[0].replace(/.*[A-Z][a-z].*/,"")
```
> captures states in the pattern N.Y. and gets rid of non-state values

```
cells.Note.value.find(/[A-Z][A-Z]/)[0]
```
> captures states in the patter NY

```
cells.Note.value.find(/Pa\.|Pa /)[0].replace(/\.|;/,"").trim()
```
> captures Pa

```
cells.Note.value.split(/Of /)[1]
```
> captures "Of..."

```
cells.Note.value.find(/[Cc]onn./)[0]
```
> captures abbreviation of Connecticut

```
cells.Note.value.find(/North .*|South .*|East .*|West .*/)[0]
```
> captures locations starting with directions
****

Location - edit cells - transform
```
value.replace(/[Ss]ee.*/,"").replace(/.*[Oo]f /,"")
```
> removes "See also.." and "of" from locations

------
## CHECK FOR ERRORS
------

[Column Name] - facet - customized facets - facet by blank - false
facet - customized facets - text length facet - [insert length]

------
## CLEANUP 
------

All - edit all columns - trim leading and trailing whitespace
```
value.replace(/[Ss]ee.*|[Dd]ate .*|[Dd]ay .*|.* [Rr]eported .*|.*[Vv]ol .*|.*[Aa]lso .*|.*&.*/,"")
```
value.replace(/.*[Bb]elonging to.*|.*[Ll]ater .*|h of.*|.*ch of|dt of .*/,"")

value.replace(/w of .*|pg.*|now .*/,"")

