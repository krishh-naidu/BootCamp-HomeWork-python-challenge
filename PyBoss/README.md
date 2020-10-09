# PyBoss

![Boss](Images/boss.jpg)

In this challenge, you get to be the _boss_. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:

* Import the `employee_data.csv` file, which currently holds employee records like the below:

```csv
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

* Then convert and export the data to use the following format instead:

```csv
Emp ID,First Name,Last Name,DOB,SSN,State
232,John,Mathews,02/24/1991,***-**-9165,ND
533,Nathan,Moore,11/19/1978,***-**-7469,ME
256,Amanda,Douglas,01/08/1990,***-**-6961,ID
189,Heather,Andrews,08/11/1976,***-**-1797,VT
284,Daniel,Hernandez,07/22/1976,***-**-7473,CO
512,Danny,Pena,01/31/1978,***-**-9878,MN
126,Gary,Knight,03/08/1994,***-**-1242,AR

```

* In summary, the required conversions are as follows:

  * The `Name` column should be split into separate `First Name` and `Last Name` columns.

  * The `DOB` data should be re-written into `MM/DD/YYYY` format.

  * The `SSN` data should be re-written such that the first five numbers are hidden from view.

  * The `State` data should be re-written as simple two-letter abbreviations.

* Special Hint: You may find this link to be helpful—[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).
