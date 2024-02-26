# HAZARD MARRIAGES

S1 is the bride

S2 is the groom

------- 

create new column → column name: sort

```
random()
```

All → edit all columns →

---- 
## NAMES
----
### S1 Name

Note → edit column → add column based on this column → column name: S1 name

```
value.find(/(?[A-Z]\S*)+(?= dt)/)[0].trim()
```

S1 name → facet → customized facet → facet null → true
```
cells.Note.value.split("  ")[0].replace(/\./,"") 
```
> a way to capture S1 names that weren't captured with the previous facet

S1 name → edit cells → transform
```
value.replace(/,?1st|2nd|2d|3rd|4th/,"").replace(/\s{2}.*|,/,'').trim()
``` 
> removes 1st, 2nd, and 3rd from the beginning of the spouses name

S1 name → edit cells → transform
```
value.replace(/\s{2}.*|,|;|:/,'')
```
> cleans up the extraneous symbols before S1 name

S1 name → edit cells → transform
```
value.replace(/[Ww]id+.*/,"")
```
> removes widow from S1 name

S1 name → edit cells → transform
```
value.replace(/[Rr]elict.*/,"")
```
> removes relict from S1 name 

S1 name → edit cells → transform
value.replace(/ dt .*| date .*| late .*| see .*| adopted .*| by .*| d .*| of .*| m to/,"")
> removes extraneous text after S1 name

#### -------------- for [to m] --------------

event → facet → text facet → for[to m]

S1 name → edit cells → transform
```
cells.Note.value.split("to m ")[1].replace(/\s{2}.*|,/,'').replace(/\./,"").trim()
```
> captures S1 names for [to m]

------ 

### S1 Father

Note → edit column → add column based on this column → column name: S1 Father
```
value.split("&")[0].split(" dt of")[1]
```

S1 Father → edit cells → transform
```
value.replace(/,?dec.*|,/,'').replace(/\s{2}.*|,/,'').replace(/\./, "").trim()
```
> gets rid of everything after S1 F name

-----

### S2 Father

Note → edit column → add column based on this column → column name: S2 Father
```
value.split("&")[1].split(" S of")[1].replace(/\./, "")
```

S2 Father → facet → customized facet → facet null → true
```
cells.Note.value.split("&")[0].split(" S of")[1].replace(/\./, "")
```
> a way to capture S2 F names that weren't captured with the previous facet

S2 Father → edit cells → transform
```
value.replace(/,?dec.*|,/,'').replace(/\s{2}.*|,/,'').trim()
```
> gets rid of everything after S2 F name

S2 Father → edit cells → transform
```
value.replace(/; .*|: .*|of .*|[Dd]ate.*|[Ss]ee .*/,"")
```
> removes extraneous text after S2 Father's name

------

### S1 Mother

Note → edit column → add column based on this column → column name: S1 Mother
```
value.split("  ")[0].split(" &")[1].replace(/\./,"") 
```

S1 Mother → facet → customized facet → facet null → true
```
cells.Note.value.split("  S of")[0].split(" &")[1].replace(/\./, "")
```
> a way to capture S1 M names that weren't captured with the previous facet

S1 Mother → edit cells → transform
```
value.replace(/,?dec|latter|both.*|,/,'').replace(/\s{2}.*|,/,'').trim()
```
> gets rid of everything after S1 Mother's name

S1 Mother → edit cells → transform
```
value.replace(/; .*|: .*|of .*|[Dd]ate.*/,"")
```
> removes extraneous text after S1 Mother's name

------

### S2 Mother

Note → edit column → add column based on this column → column name: S2 Mother
```
value.split("  S of")[1].split("  ")[0]
```
> this gives both S2 parents' names

S2 Mother → edit cells → transform
```
value.split("&")[1].split("  ")[0]
```
> captures just S2 Mother's name

S2 Mother → facet → customized facet → facet null → true
```
cells.Note.value.split("  S of")[1].split("  ")[0].split("&")[1].split("  ")[0].replace(/\./, "")
```
> a way to capture S2 M names that weren't captured with the previous facet

S2 Mother → edit cells → transform
```
value.replace(/,?dec|latter|both.*|,/,'').replace(/\s{2}.*|,/,'').trim()
```
> gets rid of everything after S2 Mother's name

S2 Mother → edit cells → transform
```
value.replace(/; .*|: .*|of .*|[Dd]ate.*|[Ss]ee .*|on .*/,"")
```
> removes extranneous text after S2 Mother's name

------
## DECEASED STATUS
------

THE LATE...

### S1 M dec

Note → edit column → add column based on this column → column name: S1 M dec
```
value.split("  S of")[0].split(" &")[1].contains(/\bdec\b/) 
```
> if it says " dec" after S1 M name, then the S1 M dec will be true

------

### S2 M dec

Note → edit column → add column based on this column → column name: S2 M dec
```
value.split("  S of")[1].split("  ")[0].split(' & ')[1].contains(/\bdec\b/) 
```
> if it says " dec" after S2 M name, then the S2 M dec will be true

------

### S1 F dec

Note → edit column → add column based on this column → column name: S1 F dec
```
value.split("&")[0].split(" dt of")[1].contains(/\bdec\b/) 
```
> if it says " dec" after S1 F name, then the S1 F dec will be true

S1 F dec → facet → text facet → false
```
cells.Note.value.split("  S of")[0].split(" &")[1].contains(/\bboth dec\b/) 
```
> if it says "both dec" after S1 parents names, then the S1 F dec will be true

------

### S2 F dec

Note → edit column → add column based on this column → column name: S2 F dec
```
value.split("  S of")[1].split("  ")[0].split(' & ')[0].contains(/\bdec\b/) 
```
> if it says " dec" after S2 F name, then the S2 F dec will be true

S2 F dec → facet → text facet → false
```
cells.Note.value.split("  S of")[1].split("  ")[0].split(' & ')[1].contains(/\bboth dec\b/) 
```
> if it says "both dec" after S2 parents names, then the S2 F dec will be true

------
## PLACE OF MARRIAGE
------

Note → edit column → add column based on this column → column name: Place of Marriage
```
value.split(/ [Aa]t /)[1]
```

Place of Marriage → edit cells → transform
```
value.replace(/\s{2}.*|,|\./,'').trim()
```
> removes anything after the Place of Marriage

------
### PREVIOUSLY MARRIED
------

### S1 Previously Married

Note → edit column → add column based on this column → column name: S1 Previously Married
```
value.contains(/([Ww]id+ow)/)
```
> captured "widow"

S1 Previously Married → edit cells → transform
```
cells.Note.value.contains(/[Rr]elict/)
```
> captured "relict"

S1 Previously Married → edit cells → transform
```
cells.Note.value.contains(/late wife of/)
```
> captured "late wife of"

MARRIED BEFORE

*DO NOT RUN (TOO AMBIGOUS)*
```
cells.Note.value.contains(/[Dd]ivorced/)
```
> captures divorcees

------
### S2 Previously Married

Note → edit column → add column based on this column → column name: S2 Previously Married
```
value.contains(/2nd|2d|3rd|4th/) 
```
> captures 2nd, 3rd, and 4th spouses

S2 Previously Married → edit cells → transform
```
cells.Note.value.contains(/[Ww]id+ower/)
```
> captured "widower"

S1 Former Spouse(s) → edit cells → transform
```
cells.Note.value.contains(/late wife\.|his late wife/)
```
> captured "late wife"


------
## FORMER SPOUSES
------

Note → edit column → add column based on this column → column name: S1 Former Spouse(s)
```
value.split(/[Ww]id+ow of/)[1].split("?.")[0]
```
> captured the S1 Former Spouse's names that appeared after "widow"

S1 Former Spouse(s) → edit cells → transform
```
cells.Note.value.split(/[Rr]elict of/)[1].split("?.")[0]
```
> captured the S1 Former Spouse's names that appeared after "relict"

S1 Former Spouse(s) → edit cells → transform
```
cells.Note.value.split(/late wife of/)[1].split("?.")[0]
```
> captured the S1 Former Spouse's names that appeared after "late wife"

S1 Former Spouse(s) → edit cells → transform
```
value.replace(/,?dec.*|,/,'').replace(/\s{2}.*|,/,'').replace(/\.|; .*/,"").trim()
```
> removes everything after S1 Former Spouse's name

-------
## NON-MEMBER
-------

### S1 Non-Member

Note → edit column → add column based on this column → column name: S1 Non-Member
```
value.contains(/[Ss]he is not a mbr/)
```

S1 Non-Member → edit cells → transform
```
cells.Note.value.contains(/[Ss]he is not a mbr/)
```
> ran on all cells and filled in blank cells

------

### S2 Non-Member

Note → edit column → add column based on this column → column name: S2 Non-Member
```
value.contains(/ [Hh]e is not a mbr/)
```

S2 Non-Member → edit cells → transform
```
cells.Note.value.contains(/ [Hh]e is not a mbr/)
```
> ran on all cells and filled in blank cells

------
## ORIGINAL MM
------

Note → edit column → add column based on this column → column name: S2 Original MM
```
value.split("MM")[0].replace(/\s{2}.*|,/,'').replace(/\.|;/,"").trim()
```

S2 Original MM → text filter → "belonging" → edit cells → transform
```
value.split("to")[1]
```
> removed everything before the meeting name

S2 Original MM → edit cells → transform
```
cells.Note.value.split("belonging to")[1].split("MM")[0].replace(/\s{2}.*|,/,'').replace(/\.|;/,"").trim()
```
> captured a few extraneous cells

S2 Original MM → edit cells → transform
```
value.replace(/to m.*/,"")
```
> removed wrong values

S2 Original MM → edit cells → transform
```
value.replace(/from /,"")
```
> removed "from"

------
## CHECK FOR ERRORS
------

[Column Name] → facet → customized facets → facet by blank → false
facet → customized facets → text length facet → [insert length]

