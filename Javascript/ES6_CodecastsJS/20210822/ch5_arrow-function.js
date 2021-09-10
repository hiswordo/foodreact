//! 如果使用function，裡面的this，就是指window了
//! 因為function是個獨立函數，沒有透過任何方法等來調用
// 真的要用的話需要在父層先定義來使用
/* const person = {
    name: 'Jelly',
    hobbies: ['sleeping', 'talking', 'reading'],
    printHobbies: function () {
        var self = this;
        // console.log(this);
        this.hobbies.map( function(hobby){
            // console.log(this);
            // console.log(this.name + " love " + hobby);
            console.log(self.name + " love " + hobby);
        })
    }
}
person.printHobbies(); */

// 然而使用arrow function，它的this會繼承父的，也就是printHobbies的
/* const person = {
    name: 'Jelly',
    hobbies: ['sleeping', 'talking', 'reading'],
    printHobbies: function () {
        this.hobbies.map(hobby => {
            console.log(this.name + " love " + hobby);
        })
    }
}

person.printHobbies(); */
