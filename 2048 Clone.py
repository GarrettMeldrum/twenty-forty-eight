import random

class twenty48:
    def __init__(self):
        # Generate the 4 x 4 grid
        self.grid = [[0] * 4 for _ in range(4)]

        # Add two initial tiles to the grid
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        # Find all empty positions
        empty_tiles = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            # Add either 2 or 4 to a random empty tile
            self.grid[i][j] = random.choice([2, 4])

    def print_grid(self):
        # Print the current state of the grid for visualization
        for row in self.grid:
            print(row)
        print()

    def slide_row_left(self, row):
        ''' Slide all non-zero tiles in a rwo to the left '''
        # Remove zeros and shift tiles to the left
        new_row = [tile for tile in row if tile != 0]
        while len(new_row) < 4:
            new_row.append(0)
        return new_row

    def merge_row_left(self, row):
        ''' Merge the row after sliding to the left '''
        for i in range(3):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
        return row

    def move_left(self):
        ''' Perform a left move '''
        moved = False
        for i in range(4):
            original_row = self.grid[i]
            # Slide row left
            new_row = self.slide_row_left(original_row)
            # Merge tiles
            new_row = self.merge_row_left(new_row)
            # Slide again to fill gaps after merging
            new_row = self.slide_row_left(new_row)
            # Update the row if there's a change
            if new_row != original_row:
                self.grid[i] = new_row
                moved = True
        if moved:
            self.add_new_tile()

    def move_right(self):
        ''' Perform a right move '''
        moved = False
        for i in range(4):
            original_row = self.grid[i]
            # Reverse the row for the right movement
            reversed_row = original_row[::-1]
            # Slide and merge on the reversed row
            new_row = self.slide_row_left(reversed_row)
            new_row = self.merge_row_left(new_row)
            new_row = self.slide_row_left(new_row)
            # Reverse back the row to restore the order
            new_row = new_row[::-1]
            # Update the row if there's a change
            if new_row != original_row:
                self.grid[i] = new_row
                moved = True
        if moved:
            self.add_new_tile()

    def transpose_grid(self):
        ''' Transpose the grid to switch rows and columns for up and down movements '''
        self.grid = [list(row) for row in zip(*self.grid)]

    def move_up(self):
        ''' Perform an up move '''
        moved = False
        # Transpose the grid to treat columns as rows
        self.transpose_grid()
        # Apply the left move logic on each "row" (now column)
        for i in range(4):
            original_row = self.grid[i]
            new_row = self.slide_row_left(original_row)
            new_row = self.merge_row_left(new_row)
            new_row = self.slide_row_left(new_row)
            if new_row != original_row:
                self.grid[i] = new_row
                moved = True
        # Transpose back to the original layout
        self.transpose_grid()
        if moved:
            self.add_new_tile()

    def move_down(self):
        ''' Perform a down move '''
        moved = False
        # Transpose the grid to treat columns as rows
        self.transpose_grid()
        # Apply the right move logic on each "row" (now columns)
        for i in range(4):
            original_row = self.grid[i]
            reversed_row = original_row[::-1]
            new_row = self.slide_row_left(reversed_row)
            new_row = self.merge_row_left(new_row)
            new_row = self.slide_row_left(new_row)
            new_row = new_row[::-1]
            if new_row != original_row:
                self.grid[i] = new_row
                moved = True
        # Transpose back to the original layout
        self.transpose_grid()
        if moved:
            self.add_new_tile()


    def game_over(self):
        ''' Check if there are no possible moves left. '''
        # Check if there are any empty tiles
        for row in self.grid:
            if 0 in row:
                return False
        # Check if there are any possible merges horizontally or vertically
        for i in range(4):
            # Only need to check up to the third element for adjacent merges
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j + 1]: # Check horizontally
                    return False
                if self.grid[j][i] == self.grid[j + 1][i]: # Check vertically
                    return False
        return True

    def play(self):
        ''' Main game loop '''
        while not self.game_over():
            self.print_grid()
            move = input("Enter move (w = up, s = down, a = left, d = right): ").lower()
            if move == 'a':
                self.move_left()
            elif move == 'd':
                self.move_right()
            elif move == 'w':
                self.move_up()
            elif move == 's':
                self.move_down()
            else:
                print("Invalid move! Please use 'w', 'a', 's', or 'd'.")
        print("Game Over!")
        self.print_grid()


game = twenty48()
game.play()