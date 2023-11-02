from src.utils.input_validator import get_valid_input
# since <export PYTHONPATH=$PYTHONPATH:$(PWD)> is run, the above import works

from src.gamelogic.number_generator import generate_random_number 
from src.gamelogic.hint_generator import provide_hint


def main():
    user_input = get_valid_input(1, 100)
    print(user_input)
    

if __name__ == '__main__':
    main()
