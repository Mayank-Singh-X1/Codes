const prompt = require("prompt-sync")();

let a= 7
let l=parseInt(a/2);
let r=parseInt(a/2);
for(let i=0; i<a/2; i++){
    let str="";
   
    for(let j=0; j<a; j++){
        if(j<=l || j>=r){
        str+='- ';
        }else{
            str+='* ';
        }
    }
    console.log(str)
    l--;
    r++;
}

let l2=parseInt(a - 1);
let r2=parseInt(a - 1);
for(let i=a/2; i>0; i--){
    let str="";
   
    for(let j=0; j<a; j++){
        if(j>=l2 && j<=r2){
        str+='* ';
        }else{
            str+='- ';
        }
    }
    console.log(str)
    l2--;
    r2--;
}



