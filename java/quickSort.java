public class quickSort {

    public static int partition(int arr[], int low, int high) {
        int pivot = arr[high];
        int i = low;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                int temp = arr[i];

                arr[i] = arr[j];
                arr[j] = temp;
                i++;
            }
        }
        int temp = arr[i];
        arr[i] = arr[high];
        arr[high] = temp;
        return i;
    }

    public static void quickS(int arr[], int low, int high) {
        if (low < high) {
            int pivot = partition(arr, low, high);

            quickS(arr, low, pivot - 1);
            quickS(arr, pivot + 1, high);
        }
    }

    public static void main(String[] args) {
        int arr[] = { 8, 5, 3, 2, 7, 1, 5, 9 };
        int n = arr.length;
        quickS(arr, 0, n - 1);

        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + ", ");
        }
        System.out.println();
    }

}
