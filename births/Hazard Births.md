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
```
value.replace(/.*[Ss] of/,"")
```
> to remove extraneous symbols before the father's name

```
value.replace(/\(.*/,"")
```
> removed the father's dad's name (i.e. Richard (s of Isaac))

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
```
value.replace(/\(.*/,"")
```
> removed the mothers's mom's name (i.e. Lisa (dt of Elizabeth))

----
### Spouse's Name

Note - edit column - add column based on this column - column name: Spouse(s)
```
value.split(/([wh] of)/)[1].replace(/\s{2}.*|,/,'').replace(/\.|;/,"").trim()
```
> captures the name after "w or h of..."

h of , w of

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

----
### Spouses Surname

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





