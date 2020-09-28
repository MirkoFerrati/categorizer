# SimpleColumnsCategorizer

### Requirements

```pip3 install xlrd openpyxl python-Levenshtein PyQt5 pandas```

The list should be all that's needed, if any module import error happen, please follow up and install the missing modules.

### How to run

we use python3, so run the entry point:

``` python3 load_show.py```

You will need to get a xlsx with your data to be categorized to test the system

- Once the window is loaded, use the menu to open a xlsx file (only 1 sheet is supported at the moment).
- The GUI can detect automatically categories once a column is selected, use LoadFromColumn for that.
- Cleanup categories using add/remove buttons.
- Use the HideGoodOnes to enable/disable a filtered display of items that are missing their category
- Select the items in the table, select the categories from the list, and click ConfirmAndWrite to put them in table
- When HideGoodOnes show nothing, it means the column has been fully categorized, save and exit


## Automatic suggestion of categories

If you EnableFancy, the system will try to propose categories automatically based on the item content that you select. This uses a simple word-distance and can help in fixing typos and case-sensitive categories.
Manual confirmation before writing is still needed.

## Shortcuts
All commands have keyboard shortcuts and each time you ConfirmAndWrite (ALT+C) a single item, the cursor moves to the next one, so that mouse can be focused only on the screen are where categories are selected.

