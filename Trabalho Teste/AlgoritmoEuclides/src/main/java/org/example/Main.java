package org.example;

import java.util.Scanner;

public class Main {
    // Método que implementa o algoritmo de Euclides
    public static int calcularMDC(int a, int b) {
        while (b != 0) {
            int resto = a % b;
            a = b;
            b = resto;
        }
        return a;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o primeiro número inteiro: ");
        int numero1 = scanner.nextInt();

        System.out.print("Digite o segundo número inteiro: ");
        int numero2 = scanner.nextInt();

        int mdc = calcularMDC(numero1, numero2);

        System.out.println("O Máximo Divisor Comum (MDC) de " + numero1 + " e " + numero2 + " é: " + mdc);

        scanner.close();
    }
}
