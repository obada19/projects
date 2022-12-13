
var di= document.getElementById("display");

var lastClicked = ''
function ud(n) {
    // d=eval(di.innerHTML += n)
    //di.innerHTML = d;

    let operators= ['+','-','*','/']
    // IF n is in operators:
    //    return False 
    if (operators.includes(n) && lastClicked === n)
        return false;

    lastClicked = n
    di.innerText += n;
}

function ans() {
    c = eval(di.innerText);
    di.innerText = c;
}

function clc() {
    disp.innerText = '';
}



document.getElementById("one").addEventListener("click", function () {
    ud('1');
});
document.getElementById("two").addEventListener("click", function () {
    ud(2);
});
document.getElementById("three").addEventListener("click", function () {
    ud(3);
});
document.getElementById("four").addEventListener("click", function () {
    ud(4);
});
document.getElementById("five").addEventListener("click", function () {
    ud(5);
});
document.getElementById("six").addEventListener("click", function () {
    ud(6);
});
document.getElementById("seven").addEventListener("click", function () {
    ud(7);
});
document.getElementById("eight").addEventListener("click", function () {
    ud(8);
});
document.getElementById("nine").addEventListener("click", function () {
    ud(9);
});
document.getElementById("zero").addEventListener("click", function () {
    ud(0);
});
document.getElementById("dec").addEventListener("click", function () {
    ud('.');
});

document.getElementById("plus").addEventListener("click", function () {
    ud('+');
});
document.getElementById("minus").addEventListener("click", function () {
    ud('-');
});
document.getElementById("multiply").addEventListener("click", function () {
    ud('*');
});
document.getElementById("divide").addEventListener("click", function () {
    ud('/');
});


document.getElementById("reset").addEventListener("click", function () {
    di.innerText = ''
});


document.getElementById("equals").addEventListener("click", function () {
    ans();
});
document.getElementById("clear").addEventListener("click", function () {
    let nums= document.getElementById("display").innerText
    document.getElementById("display").innerText = nums.slice(0,  nums.length -1);
});

