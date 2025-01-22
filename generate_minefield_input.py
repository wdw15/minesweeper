import random
import os

def generate_minefield(file_name, height=None, width=None, mine_percentage=None):
    # Set default values for height, width, and mine percentage if not provided
    if height is None:
        height = random.randint(5, 15)  # Random height between 5 and 15
    if width is None:
        width = random.randint(5, 15)   # Random width between 5 and 15
    if mine_percentage is None:
        mine_percentage = random.randint(10, 30)  # Random mine percentage between 10% and 30%

    # Calculate the total number of cells in the minefield
    total_cells = height * width
    # Calculate how many mines are needed based on the percentage
    num_mines = (total_cells * mine_percentage) // 100

    # Create a list of cells, initially filled with safe spaces ('.')
    minefield = ['.' for _ in range(total_cells)]

    # Randomly place mines in the minefield
    mine_positions = random.sample(range(total_cells), num_mines)
    for pos in mine_positions:
        minefield[pos] = '*'

    minefield_grid = []
    if width > 0:
        # Convert the list of cells back into a 2D grid (list of strings)
        minefield_grid = [minefield[i:i+width] for i in range(0, total_cells, width)]
        minefield_grid = [''.join(row) for row in minefield_grid]  # Join each row into a string

    # Prepare the text to be appended to the file
    minefield_text = f"{height} {width}\n"  # Height and width on the first line
    minefield_text += "\n".join(minefield_grid)  # Add the minefield grid

    # Append the generated minefield to the text file
    with open(file_name, "a") as file:
        file.write(minefield_text + "\n\n")  # Adding two newlines to separate each minefield

# Example usage
# test cases - trying nominal case, 0 case, large case, and single column/row cases
# also tossing in some 100% mines and 0% mine cases
try: os.remove('minefields.txt')
except: pass

generate_minefield("minefields.txt", height=10, width=10, mine_percentage=20)
generate_minefield("minefields.txt", height=0, width=0, mine_percentage=100)
generate_minefield("minefields.txt", height=1, width=10, mine_percentage=20)
generate_minefield("minefields.txt", height=100, width=100, mine_percentage=15)
generate_minefield("minefields.txt", height=5, width=5, mine_percentage=1)
generate_minefield("minefields.txt", height=50, width=50, mine_percentage=100)
generate_minefield("minefields.txt", height=25, width=25, mine_percentage=0)
generate_minefield("minefields.txt", height=50, width=1, mine_percentage=20)
