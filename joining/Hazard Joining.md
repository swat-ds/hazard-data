
# HAZARD JOINING

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
### Spouse's Name

Note - edit column - add column based on this column - column name: Spouse(s)
```
value.split(/([wh] of|[Ww]id+ow of)/)[1].replace(/\s{2}.*/,'').replace(/\..*|; .*|, .*/,"").trim()
```
> captures the name after "w or h ..." or "widow of..."

Note - text filter - "ch of"
Spouse(s) - edit cells - transform
```
value.replace(/\w+.*/,"")
```
> removes any children's names in Spouse(s)

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


*SHOULD I DO THIS (below)*

---- 
## OTHER COMPANIONS
----

Note - edit column - add column based on this column - column name: Other Companions
```
value.split(/with /)[1].replace(/\s{2}.*/,'').replace(/\..*|; .*|, .*|: .*/,"").trim()
```
> captures other companions who joined 

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
```





