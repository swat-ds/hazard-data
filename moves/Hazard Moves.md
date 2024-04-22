
# HAZARD MOVES

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

----
### Parent(s) Name

Note - edit column - add column based on this column - column name: Parent(s)
```
value.split(/ch of |s of |dt of /)[1]
```
> capture parent(s) names

----
### Father's Name

Parent(s) - edit column - add column based on this column - column name: Father
```
value.split(/&/)[0].replace(/\s{2}.*/,'').replace(/\..*|; .*|, .*|: .*/,"").trim()
```
Father - edit cells - transform
```
value.replace(/.* of /,"")
```
> removes extraneous values 

----
### Mother's Name

Parent(s) - edit column - add column based on this column - column name: Mother
```
value.split(/&/)[1].replace(/\s{2}.*/,'').replace(/\..*|; .*|, .*|: .*/,"").trim()
```
Mother - edit cells - transform
```
value.replace(/\(.*/,"")
```
> removed the mothers's mom's name (i.e. Lisa (dt of Elizabeth))

Mother - edit cells - transform
```
value.replace(/,?1st|2nd|2d|3rd|4th/,"")
```
> removes 1st, 2nd, and 3rd from the beginning of the mother's name

----
### Spouse's Name

Note - edit column - add column based on this column - column name: Spouse(s)
```
value.split(/([^c][wh] of|[Ww]id+ow of)/)[1].replace(/\s{2}.*/,'').replace(/\..*|; .*|, .*/,"").trim()
```
> captures the name after "w or h ..." or "widow of..."
> will not capture "ch of..."

Spouse(s) - edit cells - transform
```
cells.Note.value.split(/with w /)[1].replace(/\s{2}.*/,'').replace(/\..*|; .*|, .*|: .*/,"").trim()
```
> capture "with w ..."

Spouse(s) - edit cells - transform
```
value.replace(/ &| and/,";")
```
> separates spouses names with semi-colons

Spouse(s) - edit cells - transform
```
value.replace(/,?1st|2nd|2d|3rd|4th/,"").trim()
```
> removes 1st, 2nd, and 3rd from the beginning of the spouses' names

---
### Children's Name(s)

Note - edit column - add column based on this column - column name: Children
```
value.split(/ch: |dt: |s: /)[1].replace(/\s{2}.*/,'').replace(/\.|; .*|: .*/,"").trim()
```
Children - edit cells - transform
```
value.replace(/ &| and|,/,";")
```
> separates childrens names with semi-colons

------
## Source Meeting
------

> for events: prc, prcf, roc, rocf

Note - edit column - add column based on this column - column name: Source Meeting
```
value.split(/ MM/)[0].replace(/\s{2}.*/,'').replace(/\.|; .*|: .*/,"").trim()
```
> captures the meeting's name

> for events: cert

Source Meeting - edit cells - transform
```
cells.Note.value.split(/from /)[1].replace(/MM/,"").replace(/\s{2}.*/,"").replace(/\.|; .*|: .*/,"").trim()
```

------
## Destination Meeting
------

> for events: gc, gct, rqct

Note - edit column - add column based on this column - column name: Destination Meeting
```
value.split(/ MM/)[0].replace(/\s{2}.*/,'').replace(/\.|; .*|: .*/,"").trim()
```
> captures the meeting's name

> for events: cert

Destination Meeting - edit cells - transform
```
cells.Note.value.split(/to /)[1].replace(/MM/,"").replace(/\s{2}.*/,"").replace(/\.|; .*|: .*/,"").trim()
```

------
## CLEANUP 
------

All - edit all columns - trim leading and trailing whitespace
```
value.replace(/ [Ss]ee.*|[Dd]ate .*| [Dd]ay .*|.* [Rr]eported .*|.*[Vv]ol .*|.*[Aa]lso .*|.*&.*|[Aa]ge.*/,"")

value.replace(/.*[Bb]elonging to.*|.*[Ll]ater .*|h of.*|.*ch of|dt of .*|w of .*|s of .*| of .*/,"")

value.replace(/twin .*|pg .*|now .*|page .*/,"")

value.replace(/.*[Mm]onth.*| at .*|[Ww]id+ow| [Nn]ot .*| in .*/,"")

value.replace(/[0-9].*| and.*| [Aa]t .*/,"")

value.replace(/ with .*| that Meeting .*| w to .*| and .*/,"")
```






