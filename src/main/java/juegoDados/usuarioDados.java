/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package juegoDados;

import java.util.Scanner;

/**
 *
 * @author JAVIER
 */
public class usuarioDados {

    public usuarioDados() {
    }

    public static void menu() {
        System.out.println("Escriba un 1 si desea jugar \n"
                + "Escriba un 2 si desea salir ");

        try {
            int accion = leerInt();
            switch (accion) {

                case 1:
                    if (jugar()) {
                        System.out.println("Felicidades, usted ha ganado");
                    } else {
                        System.out.println("Usted ha perdido intentelo nuevamente.");
                    }

                    menu();
                    break;

                case 2:
                    System.out.println("Gracias por jugar con nosotros");
                    break;
                default:
                    System.out.println("Ingresar valor valido");
                    menu();
            }
        } catch (Exception e) {
            System.out.println("Ingresar valor valido");
            menu();
        }

    }

    public static int leerInt() {
        Scanner read = new Scanner(System.in);
        return read.nextInt();
    }

    public static boolean jugar() {
        Dado dado1 = new Dado();
        Dado dado2 = new Dado();
        dado1.setCaraSup(dado1.roll());
        System.out.println("El resultado de su primer dado es " + dado1.getCaraSup());
        dado2.setCaraSup(dado2.roll());
        System.out.println("El resultado de su segundo dado es " + dado2.getCaraSup());

        int suma = dado1.getCaraSup() + dado2.getCaraSup();
        System.out.println("Su suma es " + suma);
        if (suma == 7) {
            return true;
        } else {
            return false;
        }

    }
}
