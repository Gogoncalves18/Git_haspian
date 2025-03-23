package empresa;

public class Teste { 
    public static void main(String[] args) 
    { 
        String s1 = new String("Ola"); 
        String s2 = new String("Ola");
        String s3 = s1;
        System.out.println(s1 == s2); //PRIMEIRA COMPARAÇÃO
        System.out.println(s1.equals(s2)); //SEGUNDA COMPARAÇÃO




        System.out.println(s1 == s3); //TERCEIRA COMPARAÇÃO
    } 
}

