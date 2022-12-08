Array.prototype.max = function() {
    return Math.max.apply(null, this);
};
  
Array.prototype.min = function() {
    return Math.min.apply(null, this);
};

function maxMin(array, operation) {
    var res = "Error: invalid input(s)"
    if (operation == "max") {
        res = array.max()
    } else if (operation == "min") {
        res = array.min()
    }
    return res
}

var array = [1, 3, 5, 2, 4, 6]
var res = maxMin(array, "max")
console.log("Maximum of array " + array + " -> " + res)
var res = maxMin(array, "min")
console.log("Minimum of array " + array + " -> " + res)

var array = [35, 2, 65, 7, 8, 9, 12, 121, 33, 99]
var res = maxMin(array, "max")
console.log("Maximum of array " + array + " -> " + res)
var res = maxMin(array, "min")
console.log("Minimum of array " + array + " -> " + res)