import java.util.Scanner;

public class IF_ELSE {
    public void display(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Please enter a number");
        int i = sc.nextInt();
        /* Single IF Statement */
        //System.out.println("Example of single IF");
        if (i < 15) {
            System.out.println("Number is smaller than 15");
        }
        else{
            System.out.println("Number is greater than 15");
        }
        //System.out.println("Outside if-else block");

        /* and example*/
        if(i > 15 && i < 30){
            System.out.println ("The number is in between 15 and 30");
         }
        else {
            System.out.println("The number is less than 15 or greater than 30");
        }

        /* or example*/
        if(i > 15 || i < 30){
            System.out.println("The number is greater than 15 or less than 30");
        }

        /* Nested IF*/
            int a = 10;
            int b = 20;
            if (a==10){
                if (b==20){
                    System.out.println("Anodiam");
                }
            }

            //Switch Case statements
        int number = 44;
        String size;

        // switch statement to check size
        switch (number) {

            case 29:
                size = "Small";
                break;

            case 42:
                size = "Medium";
                break;

            // match the value of week
            case 44:
                size = "Large";
                break;

            case 48:
                size = "Extra Large";
                break;

            default:
                size = "Unknown";
                break;

        }
        System.out.println("Size: " + size);

    }


}
