let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML= counter; //set the h1 element to the most updated counter

    if (counter%10 == 0){
        alert(`Count is now ${counter}`); // introducing how ` works similar to python format strings
    // In the above code, take note of the $ sign
    }
}
document.addEventListener('DOMContentLoaded',function() { //showcasing both addEventListener and DOMContentLoaded
    document.querySelector('button').addEventListener('click', count); // the name of the function. basically this replaces the commented code in the body
}); 

