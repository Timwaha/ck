package test;
import test.Payment;

import java.security.PrivateKey;

public abstract class  Employee{
    private String name;
    protected Payment payment;

    public  Employee(String s)
    {

    }
  public void CreateE(String s) {

    }


    public String getName() {
        return name;
    }

    public String getPayType()
    {
        return getPayType();
    }
    public abstract void calcSalary();

    public abstract String getEmpType();

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
}
