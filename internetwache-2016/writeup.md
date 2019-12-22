[https://github.com/N4NU/Reversing-Challenges-List](https://github.com/N4NU/Reversing-Challenges-List)



## File Checker

openend file in IDA, examined main function. checks that '.password' exists, if not error.

Loops over charecters of the `fgetc` each time checking that we are not at the end with `feof`. Takes the input to a "magic" function and save the result to a single int32 stack variable (ORed). At the end checks that the result is 0 or smaller.

```c
void main(){
    check_file_exists();
    int result = 0;
    
    while (i <= 15){
        char c = fgetc();
        if (feof()) { return; }
        
        result = result | calculate(c);        
        i++;
    }
    
    if (result <= 0){
        puts("Congrats!");
        return;
    }
    
    puts("Wrong characters");
}
```

This means we need calculate to return 0 each time. Looking at calculate we can see an array with values at the begging, Then some sort of calculation on the current character and the matching item from the array (key). 

Looking at the input and outputs i figured that unless I put a very large number my

By trying some stuff until something sticks i found that if .password contains 0xfa*16  then the output of `calculate` is equal to `0xfa-<wanted>` which gives us an easy formula to calculate the result. 

Then when debbuging each time `calculate` returned a non zero result I knew i missed something and rechecked the corresponding value.

The final result was `IW{FILE_CHeCKa}`




