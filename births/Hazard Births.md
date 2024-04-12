# HAZARD BIRTHS

------- 

create new column - column name: sort

```
random()
```

------
## DATE
------
Year - facet - customized facets - facet by blank - false

Year - edit column - join columns - Year, Month, Day
> replace nulls with dash (-)

> write result in new column named Date

Date - edit cells - transform
```
value.replace(/--.*/," ")
```
> gets rid of (--) values

Date - edit cells - transform
```
value.replace(/-$/,"") 
```
> gets rid of (-) is there is no day

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

Father - edit cells - transform
```
value.replace(/,?1st|2nd|2d|3rd|3d|4th/,"").replace(/\s{2}.*|,/,'').trim()
```
> removes 1st, 2nd, and 3rd from the end of the father's name

----
### Father's Surname

Father - edit column - add column based on this column - column name: Father Surname
```
if(value.split(/\s+/)[-1].contains(/^jr|sr$/i), value.split(/\s+/)[-2], value.split(/\s+/)[-1])
```
> capture the last vin the Father cell
> if the last value was Jr or Sr, captures the second to last value

Father Surname - edit cells - transform
```
cells.Father.value.split(/(\w+\s+)+\S[^-]+/)[0].replace(/\w+/,"")
```
> if surname was not listed, returns a blank cell

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
### Mother's Surname

Mother - edit column - add column based on this column - column name: Mother Surname
```
value.split(/\W+/)[-1]
```

Mother Surname - edit cells - transform
```
cells.Mother.value.split(/(\w+\s+)+\S[^-]+/)[0].replace(/\w+/,"")
```
> if surname was not listed, returns a blank cell

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

New Surname - edit cells - transform
```
value.replace(/,?1st|2nd|2d|3rd|4th/,"").trim()
```

New Surname - edit cells - transform
```
value.replace(/ &| and/,";")
```
> separates different surnames with semi-colons

---
### Spouses Surname

Spouse - edit column - add column based on this column - column name: Spouses Surname
```
value.split(/\W+/)[-1]
```

Spouses Surname - edit cells - transform
```
cells.Spouse.value.split(/(\w+\s+)+\S[^-]+/)[0].replace(/\w+/,"")
```
> if surname was not listed, returns a blank cell

----
### Surname at Birth

Last Name - edit column - join columns - Last Name, Spouse Surname - column name: Birth Surname (By Spouse)
> replace nulls with space ( )

Birth Surname (By Spouse) - edit cells - transform
> write result in new column named Birth Surname (By Spouse)

Birth Surname (By Spouse) - edit cells - transform
```
value.replace(/.*\?.*|.*[Jj][Rr]*/,"").split(/(\w+\s+)+\S[^-]+/)[0].replace(/\w+/,"")
```
> removes cells w/ only a single name

> facet by blank - false - for spouse surname and surname at birth to remove all blank cells before running the code
> facet by text length - greater than 3 - for surname at birth to remove the remaining blank cells
```
filter(value.replace(/\W/," ").ngram(2),n,n.split(" ").uniques().length()!=2).length()>0
```
> returns true if the spouses surname is the same as the last name of their partners

> *explanation:* 
> - combines the columns Last Name and Spouse Surname into the column Birth Surname (By Spouse)
> - checks to see if the two names are the same
> - returns false if the names are the same

Birth Surname (By Spouse) - edit cells - transform
```
value.replace(/[^true|false].*/,"")
```
> removes any text value that is not "true" or "false"


Last Name - edit column - join columns - Last Name, Father Surname - column name: Birth Surname (By Father)
> replace nulls with space ( )

Birth Surname (By Father) - edit cells - transform
> write result in new column named Birth Surname (By Father)

Birth Surname (By Father) - edit cells - transform
```
value.replace(/.*\?.*|.*[Jj][Rr]*/,"").split(/(\w+\s+)+\S[^-]+/)[0].replace(/\w+/,"")
```
> removes cells w/ only a single name

> facet by blank - false - for father surname and surname at birth to remove all blank cells before running the code
> facet by text length - greater than 3 - for surname at birth to remove the remaining blank cells
```
filter(value.replace(/\W/," ").ngram(2),n,n.split(" ").uniques().length()!=2).length()>0
```
> returns true if the fathers surname is the same as the last name of their childs

> *explanation:* 
> - combines the columns Last Name and Father Surname into the column Birth Surname (By Father)
> - checks to see if the two names are the same
> - returns true if the names are the same

Birth Surname (By Spouse) - edit cells - transform
```
value.replace(/true/,"fae").replace(/false/,"true")
value.replace(/fae/,"false")
```
> this is needed to combine the Birth Surname (By Spouse) column and Birth Surname (By Father) column


Last Name - edit column - join columns - Birth Surname (By Spouse), Birth Surname (By Father) - column name: Surname at Birth
> replace nulls with space ( )

Surname at Birth - edit cells - transform
> write result in new column named Surname at Birth

Surname at Birth - edit cells - transform
```
value.replace(/\s.*/,"")
```
> removes duplicate values of true or false

> *explanation:* 
> - combines the columns Birth Surname (By Spouse) and Birth Surname (By Father) into the column Surname at Birth
> - uses two methods (spouses last name and fathers last name) to determine whether or not the birth record list the surname at birth


Last Name - add column based off this column - column name: Last Name 2

Last Name 2 - edit cells - transform
```
if(value == cells["Mother Surname"].value, true, null)
```
> checks if the value in the Last Name 2 cell is the same as the value in the Mother Surname cell
> if the names are the same, marks true, if they are not, marks null

Last Name - edit column - join columns - Last Name 2, Surname at Birth

> write result in Surname at Birth column

Surname at Birth - edit cells - transform
```
value.split(/\W+/)[-1]
```
> removes duplicate values of true or false

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
## IMPORTANT NOTE
------

> captured all rows that contained data pertaining to slave records
> these rows were documented to be added to a different dataset and removed from this dataset

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
value.replace(/ [Ss]ee.*|[Dd]ate .*| [Dd]ay .*|.* [Rr]eported .*|.*[Vv]ol .*|.*[Aa]lso .*|.*&.*|[Aa]ge.*/,"")

value.replace(/.*[Bb]elonging to.*|.*[Ll]ater .*|h of.*|.*ch of|dt of .*|w of .*|s of .*/,"")

value.replace(/twin .*|pg .*|now .*|page .*/,"")

value.replace(/.*[Mm]onth.*| at .*|[Ww]id+ow| [Nn]ot .*| in .*|.*[Bb]ur.*/,"")

value.replace(/[0-9].*|.*[A-Z][A-Z].*/,"")/,"")
```

