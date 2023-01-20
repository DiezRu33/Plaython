

function test(){
    text = "El número es: ";
    num1 = "";
    num2 = 100;
    for(let num1 = 0; num1 <= num2; num1++){
        if(num1 == num2){
            console.log("El utlimo numero es: " + num1);
            break;
        }
        else if(num1 > 0){
            console.log("ahora el numero es: " + num1);
            continue;
        }
    // console.log("El numero es: " + i);
    // break;
}
}

// for(let i = 0; i <= 10; i++){
//     if(i == 10){
//         console.log("El ultimo numero:" + i);
//         break;
//     } else{
//         console.log("Ahora viene el: " + i)
//     }
//     continue;
// }

test()
