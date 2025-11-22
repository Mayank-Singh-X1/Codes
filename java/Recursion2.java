public class Recursion2 {
    // public static void towerOfHanoi(int n, String src, String helper, String
    // dest) {
    // if (n == 1) {
    // System.out.println("move disk " + n + " from " + src + " to " + dest);
    // return;
    // }
    // towerOfHanoi(n - 1, src, dest, helper);
    // System.out.println("move disk " + n + " from " + src + " to " + dest);
    // towerOfHanoi(n - 1, helper, src, dest);
    // }

    // public static void reverse(String str,int index){
    // if(index ==0){
    // System.out.print(str.charAt(index));
    // return;
    // }
    // System.out.print(str.charAt(index));
    // reverse(str, index-1);
    // }

    // find first and last occurrence of character
    // public static int first=-1;
    // public static int last=-1;
    // public static void findchar(String str,char key,int index){
    // if(index==str.length()){
    // System.out.println("First occurrence: " + first);
    // System.out.println("Last occurrence: " + last);
    // return;
    // }
    // char currentChar=str.charAt(index);
    // if(currentChar==key){
    // if(first==-1){
    // first=index;
    // }else{
    // last=index;
    // }
    // }
    // findchar(str, key, index + 1); // Changed index++ to index + 1
    // }

    // check whether array is strictly increasing or not
    // public static boolean Strictinc(int[] arr, int index){
    // if(index == arr.length-1){
    // return true;
    // }
    // if(arr[index] < arr[index+1]){
    // return Strictinc(arr, index+1);
    // }else{
    // return false;
    // }
    // }

    // Move a given cahracter to end of string
    // public static void moveallX(String str, int idx, int count, String newstr) {
    //     if (idx == str.length()) {
    //         for (int i = 0; i <= count; i++) {
    //             newstr += 'x';
    //         }
    //         System.out.println(newstr);
    //         return;
    //     }
    //     char currentChar = str.charAt(idx);
    //     if (currentChar == 'x') {
    //         count++;
    //         moveallX(str, idx + 1, count, newstr);
    //     } else {
    //         newstr += currentChar;
    //         moveallX(str, idx + 1, count, newstr);
    //     }
    // }

    // Move a given number to end of array without creating another variable (left right pointer method)
    // public static void moveZeroes(int[] nums) {       
    //     if (nums == null || nums.length < 2) {
    //         return;
    //     }
    //     int left = 0;
    //     for (int right = 0; right < nums.length; right++) {
    //         if (nums[right] != 0) { 
    //             int temp = nums[right];
    //             nums[right] = nums[left];
    //             nums[left] = temp;
    //             left++;
    //         }
    //     }
    //     for(int i=0;i<nums.length;i++){
    //         System.out.print(nums[i]+" ");
    //     }
    // }

    //remove Duplicates from given string
    // public static boolean[] map =new boolean[26];
    // public static void removeDuplicate(String str, int idx, String newstr){
    //     if(idx==str.length()){
    //         System.out.println(newstr);
    //         return;
    //     }
    //     char currentchar=str.charAt(idx);
    //     if(map[currentchar-'a']){
    //         removeDuplicate(str, idx+1, newstr);
    //     }else{
    //         newstr+=currentchar;
    //         map[currentchar-'a']=true;
    //         removeDuplicate(str, idx+1, newstr);
    //     }
    // }

    //print all subsequences of String
    // public static void Subsequence(String str, int idx, String newstr){
    //     if(str.length()==idx){
    //         System.out.println(newstr);
    //         return;
    //     }
    //     char currchar=str.charAt(idx);
    //     Subsequence(str, idx+1, newstr+currchar); // want to be added in string
    //     Subsequence(str, idx+1, newstr);// don't want to be added in string
    // } 

    //print possible combinations of keypad mobile
    public static String [] keypad={".","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"};

    public static void Combination(String str, int idx, String combo){
        if(str.length()==idx){
            System.out.println(combo);
            return;
        }
        char currchar=str.charAt(idx);
        String mapping=keypad[currchar-'0'];
        for(int i=0;i<mapping.length();i++){
            Combination(str, idx+1, combo+mapping.charAt(i));
        }
    }

    public static void main(String[] args) {

        // Tower Of Hanoi
        // int n = 3;
        // towerOfHanoi(n, "S", "H", "D");

        // Print word in reverse
        // String a="leh reh lund keh";
        // reverse(a,a.length()-1);

        // Find first and last index of character
        // String a="Sanat Clausahk";
        // findchar(a, 'a', 0);

        // check whether array is strictly increasing or not
        // int arr[]={1,2,3,4,5};
        // boolean isStrictlyIncreasing = Strictinc(arr, 0);
        // System.out.println("Is array strictly increasing? " + isStrictlyIncreasing);

        // Move a given cahracter to end of string
        // String str = "axbxxcd";
        // moveallX(str, 0, 0, "");

        // Move a given number to end of array without creating another variable
        // int []num={0,1,2,0,0,3};
        // moveZeroes(num);

        //remove Duplicates from given string
        // String s="abbcdda";
        // removeDuplicate(s, 0, "");

        //print all subsequences of String
        // String a="abcd";
        // Subsequence(a, 0, "");

        //print possible combinations of keypad mobile
        String a="101";
        Combination(a, 0, "");     
    }

}
