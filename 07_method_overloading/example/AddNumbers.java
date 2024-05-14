// METHOD OVERLOADING => It is the action of creating severals methods with the
// same objective or purpose, naming them with the same name (different numbers
// or parameters types for each method), executing one method or another according 
// to the number or type of parameters. It provide to the user a more intuitive 
// and adaptable interface.

package example;

public class AddNumbers {  // Utility class.

    //                   Integer parameter.
    //                      ⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽
    //                      ↓         ↓
    public static void add(int num1, int num2) {  //                     <-╻
        int result = num1 + num2;  //                                      │
        System.out.print(num1 + " + " + num2 + " = " + result + "\n");  // │	Methods with the
    }  //                                                                  │ => same name and 
    //                                                                     │    objective (add numbers).
    //                                                                     │    
    public static void add(double num1, double num2) {  //               <-╹
    //                       ↑            ↑
    //                       ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺
    //                      Double parameter.

        double result = num1 + num2;
        System.out.print(num1 + " + " + num2 + " = " + result + "\n");
    }
}
