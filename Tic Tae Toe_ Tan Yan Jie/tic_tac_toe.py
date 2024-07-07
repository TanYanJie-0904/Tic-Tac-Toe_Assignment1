class TicTacToe:
    def __init__(self):
        self.ttt = {'top-l':' ','top-c':' ','top-r':' ','middle-l':' ','middle-c':' ','middle-r':' ','bottom-l':' ','bottom-c':' ','bottom-r':' '}
        self.ans1 = ''
        self.once_location = []
        self.win_conditions = [
            ['top-l', 'top-c','top-r'],
            ['middle-l', 'middle-c','middle-r'],
            ['bottom-l', 'bottom-c','bottom-r'],
            ['top-l', 'middle-l','bottom-l'],
            ['top-c','middle-c','bottom-c'],
            ['top-r','middle-r','bottom-r'],
            ['top-l', 'middle-c','bottom-r'],
            ['bottom-l', 'middle-c','top-r']
        ]

    def get_starting_player(self):
        while self.ans1 not in ['x', 'o']:
            print("Players can choose 'x' or 'o'")
            print("Please select which Player starts first.")
            self.ans1 = input().lower()
            if self.ans1 not in ['x', 'o',]:
                print("Wrong input! Please try again.\n")

    def print_start_board(self):
        print('  Top-Left ', '|', '  Top-Center ', '|', '  Top-Right ')
        print('- - - - - - + - - - - - - - + - - - - - -')
        print('Middle-Left', '|', 'Middle-Center', '|', 'Middle-Right')
        print('- - - - - - + - - - - - - - + - - - - - -')
        print('Bottom-Left', '|', 'Bottom-Center', '|', 'Bottom-Right')
        print("\n")

    def print_board(self):
        print(self.ttt['top-l'], '|', self.ttt['top-c'], '|', self.ttt['top-r'])
        print('- + - + -')
        print(self.ttt['middle-l'], '|', self.ttt['middle-c'], '|', self.ttt['middle-r'])
        print('- + - + -')
        print(self.ttt['bottom-l'], '|', self.ttt['bottom-c'], '|', self.ttt['bottom-r'])
        print("\n")

    def check_winner(self):
        for condition in self.win_conditions:
            if self.ttt[condition[0]] == self.ttt[condition[1]] == self.ttt[condition[2]] != ' ':
                return self.ttt[condition[0]]
        return None

    def play_game(self):
        self.get_starting_player()
        print("OK, " + str(self.ans1) + " you first!")
        print("\n1:Top-Left"+
              "\n2:Top-Center"+
              "\n3:Top-Right"+
              "\n4:Middle-Left"+
              "\n5:Middle-Center"+
              "\n6:Middle-Right"+
              "\n7:Bottom-Left"+
              "\n8:Bottom-Center"+
              "\n9:Bottom-Right\n\n")
        self.print_start_board()
        i = 0
        while i < 9:
            current_player = self.ans1 if i % 2 == 0 else 'o' if self.ans1 == 'x' else 'x'
            print(f"Player {current_player}'s turn.")
            location = input("Which place you want to put.")

            if location not in self.once_location and location.isdigit() and 1 <= int(location) <= 9:
                self.once_location.append(location)
                match location:
                    case '1':
                        self.ttt['top-l'] = current_player
                    case '2':
                        self.ttt['top-c'] = current_player
                    case '3':
                        self.ttt['top-r'] = current_player
                    case '4':
                        self.ttt['middle-l'] = current_player
                    case '5':
                        self.ttt['middle-c'] = current_player
                    case '6':
                        self.ttt['middle-r'] = current_player
                    case '7':
                        self.ttt['bottom-l'] = current_player
                    case '8':
                        self.ttt['bottom-c'] = current_player
                    case '9':
                        self.ttt['bottom-r'] = current_player

                self.print_board()

                winner = self.check_winner()
                if winner:
                    print(f"Congratulations! Player {winner} wins!")
                    return

                if ' ' not in self.ttt.values():
                    print("Draw!")
                    return

                i += 1
            else:
                print("Invalid input or place already taken. Please select again.\n")

        print("Game over! It's a draw!")
