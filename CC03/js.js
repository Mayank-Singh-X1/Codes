let box= document.querySelector('.right')
let line1= document.querySelector('.upper')
let line2= document.querySelector('.middle')
let line3= document.querySelector('.lower')

let flag=0
if(flag){
box.addEventListener('click', ()=>{
    line1.style.transform='rotate(45deg)'
    line2.style.display='none'
    line3.style.transform='rotate(-45deg)'
    box.style.justifyContent='center'
    box.style.alignItems='center'
    flag=1
    
})
}else{
    flag=0
    box.addEventListener('click', ()=>{
    line1.style.transform='rotate(0deg)'
    line2.style.display='1'
    line3.style.transform='rotate(0deg)'
})
}