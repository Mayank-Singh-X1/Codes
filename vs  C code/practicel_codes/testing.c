#include <stdio.h>
int main() {
    FILE *file;
    char data[20];
    // Open file in read mode
    file = fopen("example.txt", "r");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    // Move the file pointer to the 10th byte from the beginning
    fseek(file, 10, SEEK_SET);
    // Read data from the file
    fgets(data, 10, file);
    printf("Data from 10th byte: %s\n", data);

    // Move the pointer to 5 bytes before the end of the file
    fseek(file, -5, SEEK_END);

    // Read data from that position
    fgets(data, 5, file);
    printf("Data 5 bytes before end: %s\n", data);

    // Close the file
    fclose(file);

    return 0;
}


