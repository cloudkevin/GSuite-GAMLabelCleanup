# GSuite-LabelCleanupPrep

First use GAM to export labels to CSV: ```./gam user <username> show labels onlyuser > userLabels.csv```

Once that list has been created, use this to cleanup the list to only display label names: ```python3 labelcleanup.py```

After entering the path to the GAM exported CSV the script will overwrite the original file with the output
