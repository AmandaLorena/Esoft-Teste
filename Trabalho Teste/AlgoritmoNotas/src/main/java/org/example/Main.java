package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double soma = 0;

        // Ler as 4 notas
        for (int i = 1; i <= 4; i++) {
            System.out.print("Digite a nota " + i + ": ");
            double nota = scanner.nextDouble();
            soma += nota;
        }

        double media = soma / 4;

        System.out.println("Média do aluno: " + media);

        // Verificar situação
        if (media >= 7.0) {
            System.out.println("Situação: Aprovado por média");
        } else if (media >= 4.0) {
            System.out.println("Situação: Prova final");
        } else {
            System.out.println("Situação: Reprovado");
        }

        scanner.close();
    }
}
