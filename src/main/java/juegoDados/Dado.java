/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package juegoDados;

import java.util.Random;

/**
 *
 * @author JAVIER
 */
public class Dado {
    private int caraSup;

    public Dado() {
    }

    public Dado(int caraSup) {
        this.caraSup = caraSup;
    }

    public int getCaraSup() {
        return caraSup;
    }

    public void setCaraSup(int caraSup) {
        this.caraSup = caraSup;
    }
    
    public int roll(){
        Random azar = new Random();
        caraSup= azar.nextInt(6)+1;
        return caraSup;
    }
    
}
