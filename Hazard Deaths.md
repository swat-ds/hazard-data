# Hazard Deaths
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

Date → edit cells → transform
```
value.replace(/--/," ")
```
> gets rid of (--) values

---- 
## NAMES
----
### Father's Name

Note - edit column - add column based on this column - column name: Father
```
value.split(/&/)[0].replace(/.*w of.*|.*[^c]h of.*|.*[Ww]id+ow of.* /,"").replace(/\.|;.*/,"")
```
Father - edit cells - transform
```
value.replace(/.*of /,"").replace(/\s{2}.*|,/,"").replace(/\.|;.*/,"").trim()
```
> removes extraneous values 

Father - edit cells - transform
```
value.replace(/,?1st|2nd|2d|3rd|3d|4th/,"").replace(/\s{2}.*|,/,'').trim()
```
> removes 1st, 2nd, and 3rd from the end of the father's name

----
### Mother's Name

Note - edit column - add column based on this column - column name: Mother
```
value.split(/&/)[1].replace(/\s{2}.*|,/,'').replace(/\.|;.*/,"").trim()
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
value.split(/([^c][wh] of|[Ww]id+ow of)/)[1].replace(/\s{2}.*|,/,'').replace(/\.|;/,"").trim()
```
> captures the name after "w or h of..." or "widow of..."
> will not capture "ch of..."

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

----
### Sibling's Name

Note - edit column - add column based on this column - column name: Sibling(s)
```
value.split(/[Tt]win of /)[1].replace(/\s{2}.*|,/,'').replace(/\.|;/,"").trim()
```
> captures twins 
> there are just over 100 values for this, still capture?

-------
## NON-MEMBER
-------

Note - edit column - add column based on this column - column name: Non-Member
```
value.contains(/[Nn]ot a mbr/)
```
> captures non-members

-------
## AGE
-------
Note - edit column - add column based on this column - column name: Age of Death
```
value.split(/[Aa]ge/)[1].replace(/\s{2}.*|y/,'').replace(/\..*|;.*|,.*/,"").trim()
```
Age of Death - edit cells - transform
```
value.replace(/d |\s{1}.*/,"")
```
> removes day and month values

Age of Death - edit cells - transform
```
value.replace(/m/," months")
```
> states if the date is in months

Age of Death - edit cells - transform
```
value.replace(/d/," days")
```
> states if the date is in days

-------
## BURIAL LOCATION
-------

Note - edit column - add column based on this column - column name: Burial Location
```
value.split(/Bur; /)[1].replace(/\s{2}.*/,'').replace(/\..*|;.*|,.*/,"").trim()
```

------
## CLEANUP 
------

All - edit all columns - trim leading and trailing whitespace
```
value.replace(/ [Ss]ee.*|[Dd]ate .*| [Dd]ay .*|.* [Rr]eported .*|.*[Vv]ol .*|.*[Aa]lso .*|.*&.*|[Aa]ge.*/,"")

value.replace(/.*[Bb]elonging to.*|.*[Ll]ater .*|h of.*|.*ch of|dt of .*|w of .*|s of .*/,"")

value.replace(/twin .*|pg .*|now .*|page .*/,"")

value.replace(/.*[Mm]onth.*| at .*|[Ww]id+ow| [Nn]ot .*| in .*|.*[Bb]ur.*/,"")

value.replace(/[0-9].*|[Ll]ot.*/,"")/,"")
```




