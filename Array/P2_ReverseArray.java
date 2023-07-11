package Array;

import java.util.Scanner;

public class P2_ReverseArray {
    public static void printArray(int[] inArray){
        int size = inArray.length;
        for(int i=0; i<size; i++){
            System.out.print(inArray[i]+" ");
        }
    }

    public static int[] inputArray(){
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the Size of the Array : ");
        int n = scan.nextInt();

        int[] array = new int[n];
        for(int i=0; i<n; i++){
            System.out.print("Enter the Number : ");
            int ele = scan.nextInt();
            array[i] = ele;
        }
        scan.close();
        return array;
    } 

    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int[] arr1 = inputArray();
        printArray(arr1);

        


        scan.close();
    }
}