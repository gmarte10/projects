package cs410.uno;

import java.util.Scanner;

/*
Used to run one game. Asks user for info. Outputs the game results in the terminal
 */

public class RunOneGame {
    public static void main(String[] args)  {
        Scanner in = new Scanner(System.in);

        System.out.println("Number of players: ");
        int countPlayers = in.nextInt();

        System.out.println("Number of of cards per player: ");
        int countInitialCardsPerPlayer = in.nextInt();

        System.out.println("Number of color per digit: ");
        int countDigitCardsPerColor = in.nextInt();

        System.out.println("Number of special cards per color: ");
        int countSpecialCardsPerColor = in.nextInt();

        System.out.println("Number of wild cards: ");
        int countWildCards = in.nextInt();

        GameState gameState = new GameState(countPlayers,
                countInitialCardsPerPlayer,
                countDigitCardsPerColor,
                countSpecialCardsPerColor,
                countWildCards);
        gameState.runOneGame();
    }
}
