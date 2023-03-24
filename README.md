
# Random Password Generator

This is a simple Python script that generates a random password based on user-defined parameters. The user can specify the length of the password and whether to include uppercase letters, digits, and symbols. The script uses the "click" library to create command-line options for easy customization.




## Installation

   1. Clone the repository to your local machine:
```bash
    git clone https://github.com/Ire-loop/password-generator.git
```
   2. Navigate to the project directory:
```bash
  cd password-generator
```
   3. Install the required dependencies:
```bash
  pip install -r requirements.txt
```

## Usage
To use the script, run the following command:

```
  python password_generator.py
```
This will generate a password with the default length of 8 characters, including uppercase letters, digits, and symbols. You can customize the options using the following command-line arguments:

• --length: The length of the password (default is 8).

• --uppercase/--no-uppercase: Whether to include uppercase letters (default is True).

• --digits/--no-digits: Whether to include digits (default is True)

• --symbols/--no-symbols: Whether to include symbols (default is True).

For example, to generate a password with a length of 12 characters and no uppercase letters:
```CSS
  python password_generator.py --length 12 --no-uppercase
```
## Contributing
If you find a bug or have a feature request, please open an issue. Contributions are also welcome via pull requests.

## Licence
This project is licensed under the MIT License.
