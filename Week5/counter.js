if(!localStorage.getItem('counter')){ //checking the local storage if there isnt a variable named counter
    // if there is not:
    localStorage.setItem('counter', 0);
}

function count() {
    let counter = localStorage.getItem('counter'); // get the counter from the local storage
    counter++;
    document.querySelector('h1').innerHTML= counter; //set the h1 element to the most updated counter
    localStorage.setItem('counter', counter); // reassigning counter from the local storage to be the counter displayed by HTML.

}
document.addEventListener('DOMContentLoaded',function() { //showcasing both addEventListener and DOMContentLoaded
    document.querySelector('h1').innerHTML = localStorage.getItem('counter'); // Essentially, this saves the counter into the local storage. Set the counter.html to be the most updated;
    document.querySelector('button').addEventListener('click', count); // the name of the function. basically this replaces the commented code in the body
    setInterval(count,1000); //increment the count by 1 for every second


}); 

