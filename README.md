# Vochain-process-fetch-test

Another one of Aragon's solutions is Vochain, a layer 2 protocol tailored for enabling gassless voting for the blockchain and traditional worlds.

Visit https://docs.vocdoni.io/#/architecture/services/gateway to know more about the gateway that will enable you to fetch data from Vochain.

### Notes
The requirements.txt file should list all Python libraries that your notebooks depend on, and they will be installed using:

```
pip install -r requirements.txt
```
### Run the Script

Use Python 3 (version 3.8.6) to run the script

```
python vochain_script.py
```

### Result
The result will be two independent .csv files. One containing information about the processes and the entity the belong to and the second one containing the details of the votes (envelopes) in each of the processes.

```
process.csv
test.csv
```
