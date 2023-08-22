public class Main {
    public static void main(String[] args) {
        //For loop
        int i = 0;
        for (i=0; i <=10; i++){
            System.out.println("(For loop) The number is : "+i);
        }
        //WHILE Loop
        i=0;
        while(i<=10){
            System.out.println("(while loop) The number is : "+ i);
            i++;
        }
        //DO_WHILE Loop
        i=0;
        do{
            System.out.println("(do-while) The number is : "+i);
            i++;
        }while (i <=10);
    }
}