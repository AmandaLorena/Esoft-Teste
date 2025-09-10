package org.example;

import java.util.Scanner;

public class Main {

    // Método para calcular fatorial
    public static long fatorial(int num) {
        long resultado = 1;
        for (int i = 2; i <= num; i++) {
            resultado *= i;
        }
        return resultado;
    }

    // Método para calcular a combinatória
    public static long combinatoria(int n, int k) {
        return fatorial(n) / (fatorial(k) * fatorial(n - k));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o valor de n: ");
        int n = scanner.nextInt();

        System.out.print("Digite o valor de k: ");
        int k = scanner.nextInt();

        if (n < k) {
            System.out.println("Erro: o valor de n deve ser maior ou igual a k.");
        } else {
            long resultado = combinatoria(n, k);
            System.out.println("C(" + n + ", " + k + ") = " + resultado);
        }

        scanner.close();
    }
}
