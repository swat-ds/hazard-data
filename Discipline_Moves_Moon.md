# Discipline_HazardThru37 Transformation History

This document outlines the steps taken during the data cleaning and extraction process using OpenRefine.

## Column Additions

### 1. Extracted Reason
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*(mcd|mou|mos|jas).*/).toString()
  ```
- **Description:** Created a new column `Reason` capturing keywords such as `mcd`, `mou`, `mos`, and `jas` from the `Note` field.

### 2. Extracted Previous Surname
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*(latel?y?|formerl?y?)\s+(.*?)(?=[.;]).*/)[1].toString()
  ```
- **Description:** Extracted previous surnames based on terms like `formerly` or `lately`.

### 3. Extracted Father's Name
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*\b(dt|s|ch)\s+of\s+(.*?)(?=[;&]).*/)[1].toString()
  ```
- **Description:** Identified the father's name when patterns like `dt of`, `s of`, or `ch of` were present.

### 4. Extracted Mother's Name
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*\b(dt|s|ch)\s+of\s+(.*?)\s+&\s+(.*?)(?=[;&]).*/)[2].toString()
  ```
- **Description:** Pulled the mother's name when two parents were listed with an ampersand.

### 5. Extracted Spouse
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*\b(w|h|mou|mos|mcd);?\s+t?o?f?w?i?t?h?\s+(.*?)(?=[.;]).*/)[1].toString()
  ```
- **Description:** Captured the spouse's name, accounting for abbreviations like `w`, `h`, `mos`, etc.

### 6. Extracted Meeting Involvement
- **Source column:** `Note`
- **GREL expression:**
  ```grel
  value.match(/.*(Minute|at)\s+t?f?r?o?m?(.*?)\s+(MM)(?=[.;]).*/)[1].toString()
  ```
- **Description:** Extracted mentions of Monthly Meetings (`MM`) and involvement (e.g., “Minute to…” or “at…”).

---

## Column Reordering

Reordered the columns to fit the order provided on the work plan.

---