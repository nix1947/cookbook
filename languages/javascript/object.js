/*
Basic of objects. 
Javascript use prototypal chain to implement OOP

*/


function Person(name, age, interest) {
    var obj = {
        name: name,
        age: ag, 
        interest: interest
       
    }

    return obj;

}

var p1 = Person()

// Create a basic object. 
// Create an object 
var Person = {}  // ES6 has class keyword which is syntatic sugar to this one. 

// Hard coded object,
var Person = {
    name: "manoj",
    age: 32, 
    gender: 'male',
    interests: ["Football", 'game'],
    bio: function () {
        this.name + ' '  + this.age + ' ' + this.interests[0]
    }
}





