/*

file: calculator.java 
author: James Henry 
functionality: the user will input the two inputs in decimal. To convert to binary, Java has a built in integer to binary 
string function. This function returns a string representation of the integer as an unsigned int in base 2 (binary). 
Once the script computes the output, I programmed it to format the binary representation and decimal representation. 

*/


import java.util.Scanner; // java util 

public class calculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        try {
            // User inputs num1
            System.out.print("Enter the first number (decimal): ");
            int num1 = input.nextInt();

            // User inputs num2
            System.out.print("Enter the second number (decimal): ");
            int num2 = input.nextInt();

            // Perform addition
            int sum = num1 + num2;

            // Determine max bit length
            int maxBits = Math.max(
                Integer.toBinaryString(num1).length(),
                Integer.toBinaryString(num2).length()
            );

            // Pad binary strings
            String bin1 = String.format("%" + maxBits + "s", Integer.toBinaryString(num1)).replace(' ', '0');
            String bin2 = String.format("%" + maxBits + "s", Integer.toBinaryString(num2)).replace(' ', '0');
            String binSum = String.format("%" + maxBits + "s", Integer.toBinaryString(sum)).replace(' ', '0');

            // Output in decimal
            System.out.println("\n--- Decimal Output ---");
            System.out.println("First number: " + num1);
            System.out.println("Second number: " + num2);
            System.out.println("Sum: " + sum);

            // Output in binary with MSB alignment
            System.out.println("\n--- Binary Output (MSB aligned) ---");
            System.out.println("First number: " + bin1);
            System.out.println("Second number: " + bin2);
            System.out.println("Sum: " + binSum);
        } finally {
            input.close();
        }
    }
}
