# GSuite-GAMLabelCleanup

## Usage
First use GAM to export labels to CSV: ```./gam user <username> show labels onlyuser > userLabels.csv```

Once that list has been created, use this to cleanup the list to only display label names: ```python3 labelcleanup.py```

After entering the path to the GAM exported CSV the script will overwrite the original file with the output

If you would like to delete the labels you'll need to remove the index column from the output CSV and add a header before using with GAM (You could also use `~0` as the column name for GAM but I recommend validation and cleanup)

Delete the labels: ```./gam csv <csvFilePath> gam user <userEmail> delete label ~labelName```

## Requirements
Python3  
Pandas ```pip3 install pandas```
