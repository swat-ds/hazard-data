# Moon Discipline Moves (2)

This document outlines the second attempt at matching with GREL regular expressions. 
The first 5 entries are previously existing fields which have been updated using feedback.
Entries 6-8 are new and attempt to capture the surnames of father, mother, and spouse entries, when possible.

## Column Additions

### 1. Extracted Reason
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/\b.*(mcd|mou|mos|jas).*/)[0]
  ```
- **Description:** Created a new column `Reason` to capture keywords like `mcd`, `mou`, `mos`, or `jas`.

### 2. Extracted Previous Surname
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*\b(form|late)\w*\s(([A-Z](\w+|\.?)+)?\s?(([A-Z](\w+|\.?)+)?).*/)[2]
  ```
- **Description:** Extracted previous surname using indicators such as `formerly` or `late`.

### 3. Extracted Father's Name
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*\b((?i)s|dt|ch)\s+of\s+([A-Z]\w+).*/)[1]
  ```
- **Description:** Identified the father's name from structured mentions like `s of`, `dt of`, or `ch of`.

### 4. Extracted Mother's Name
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*\b((?i)s|dt|ch)\s+of\s+([A-Z]\w+)\s*([A-Z](\w+|\.)+)*\s+(&|and)\s+([A-Z]\w+).*/)[5]
  ```
- **Description:** Captured the mother’s name when mentioned alongside the father using `&` or `and`.

### 5. Extracted Spouse
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*(?:\b(w|h)\s*o?f?|(?:mcd|mou|mos)\W\s*(?:to|with))\s*([A-Z]\w*).*/)[1]
  ```
- **Description:** Added a `Spouse` column capturing mentions of a spouse via patterns like `w of`, `h of`, or `mcd to`.

### 6. Extracted Father's Surname
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*\b((?i)s|dt|ch)\s+of\s+([A-Z]\w+)\s+([A-Z]\w*).*/)[2]
  ```
- **Description:** Extracted the father’s surname when given as two capitalized names.

### 7. Extracted Mother's Surname
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*\b((?i)s|dt|ch)\s+of\s+([A-Z]\w+)\s*([A-Z](\w+|\.)+)*\s+(&|and)\s+([A-Z]\w+)\s+([A-Z]\w*).*/)[6]
  ```
- **Description:** Extracted the mother’s surname when mentioned with the father’s name in full.

### 8. Extracted Spouse's Surname
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*(?:\b(w|h)\s*o?f?|(?:mcd|mou|mos)\W\s*(?:to|with))\s*([A-Z]\w*)\s*([A-Z]\w*).*/)[2]
  ```
- **Description:** Added a `Spouse's Surname` column when both the first and last name of a spouse appeared.

---
