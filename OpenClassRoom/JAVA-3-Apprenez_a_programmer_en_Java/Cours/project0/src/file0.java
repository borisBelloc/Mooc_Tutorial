import java.util.Scanner;

public class file0 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        System.out.println(" You have just run HelloWorld !");       

        // Caster int -> double (convertir entier en decimal)
        int var1 = 15, var2 = 5;
        double resultat = (double)(var1) + (double)(var2);
        System.out.println(resultat);
        // Caster int -> String
        int i = 12;
        String j = new String();
        j = j.valueOf(i);
    	// String -> int 
        int k = Integer.valueOf(j).intValue(); // Il existe des équivalents a intValue()pour les autres types numériques :floatValue(),doubleValue()…
        
        //
        double nombreA = 1000000d;
        // Peut s'écrire ainsi
        double nombreB = 1__000_000d; // Le nombre d'underscore n'a pas d'importance
        System.out.println("nombreB " + nombreB);

        
        Scanner sc = new Scanner(System.in);
//        input String
        System.out.println("Veuillez saisir un mot :");
        String str = sc.nextLine();
        System.out.println("Vous avez saisi : " + str);        
        
//        input int
        System.out.println("Veuillez saisir un nombre :");
        int int1 = sc.nextInt();
        System.out.println("Vous avez saisi le nombre : " + int1);
//        fonctionne avec tous les type :
        double d = sc.nextDouble();
        long l = sc.nextLong();
        byte b = sc.nextByte();
	}

	
	  public static void Scan() {
		    Scanner sc = new Scanner(System.in);
		    System.out.println("Saisissez un entier : ");
		    int i = sc.nextInt();
		    System.out.println("Saisissez une chaîne : ");
		    //On vide la ligne avant d'en lire une autre
		    sc.nextLine();
		    String str = sc.nextLine();      
		    System.out.println("FIN ! ");
	
	  }
}
