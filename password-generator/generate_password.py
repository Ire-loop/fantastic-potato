import click
import random
import string

@click.command()
@click.option('--length', default=8, help='Length of password')
@click.option('--uppercase/--no-uppercase', default=True, help='Include uppercase characters')
@click.option('--digits/--no-digits', default=True, help='Include digits')
@click.option('--symbols/--no-symbols', default=True, help='Include symbols')


def generate_password(length, uppercase, digits, symbols):
    
    while True:
        characters = string.ascii_lowercase
        if uppercase:
            characters += string.ascii_uppercase
        if digits:
            characters += string.digits
        if symbols:
            characters += string.punctuation
        
        
        password = ''.join(random.choice(characters) for _ in range(length))
        click.echo(password)

        choice = input("Press 'x' to exit \n")
        if choice == 'x':
            break
    

if __name__ == '__main__':
    generate_password()
