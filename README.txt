# Xinger

Xing.com employee enumeration tool for OSINT 

## About Xinger

Xing.com is a python tool designed to enumerate through a companies entire employee list to gather each employee's name, role, and Xing Profile Link. Xinger utilizes multiple jQuery get requests to collect and parse, then present or save a companies workforce.

## Installation

```
git clone https://github.com/MarviMalware/Xinger.git
```
## Recommended Python Version:

Xinger currently only supports **Python 3**
  * The recommended version for Python 3 is **3.7.x**

## Dependencies

Xinger currently depends on the `requests`, `re`, `time`, and `argparse` python modules.

To install utilizing the requirements.txt:

  * Windows Installation:
```bash
python -m pip install -r requirements.txt
```
  * Linux Installation:
```bash
sudo pip install -r requirements.txt
```

## Usage

| Long Form | Short Form | Description                                          |
| --------- | :--------: | :--------------------------------------------------- |
| --file    | -f         | Specifies a file location and name to save the results to. |
|--silent   | -s         | Hides console output.                                |
|--help     |-h          | Shows help message.                                   |

## Examples
  * Prints an enumerated Employee List within the console.
```bash
python Xinger.py https://www.xing.com/company/xing
```
  * Prints an enumerated Employee List within the console, then saving it to a specified file.
```bash
python Xinger.py -f employeeList.txt https://www.xing.com/company/xing
```
  * Saves the resulting list to a specified file without printing anything to the console. (Silences the banner aswell)
```bash
python Xinger.py -s -f employeeList.txt https://www.xing.com/company/xing
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)