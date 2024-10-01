
// modern way of JS, put in script beginning or function beginning
// requires variable declaration
"use strict"; 

const   MY_NAME     = "Babel";
let     message     = "hello kitty";
let     pl_inf      = Infinity;
let     not_num     = NaN;
let     huge_num    = 87191273981724412312312n;
let     n_message   = `elo ${message}`; // !! backtick
let     checking    = true;
let     empty       = null; // use this to indicate empty variable
let     nondef      = undefined;

let     result      = null
const   dzejson     = '{"funkcja": \
                        { "arguments": "a=5; b; c" \
                        , "body": "return c=a*b" \
                        } \
                    }';
let     fruits      = 5;
let     veggies     = 7;

// alert(message);
// alert(pl_inf);
// alert(not_num);
// alert(huge_num);
// alert(typeof(n_message));
// alert(`Max value of variable is\n ${Number.MAX_VALUE}`)

// let elo = JSON.parse(dzejson);
// alert(elo.funkcja.arguments);
// alert("string" + " another string");

// result = prompt("hello give me", 100); //its better to give default (IE)
// alert(`before conversion ${typeof(result)}`);
// result = Number(result);
// alert(`after conversion ${typeof(result)}`);
// alert(`you gave ${result}`);
// result = confirm(`is that really true that you gave ${result}`);
// alert(`you said that it's ${result} and in integer language it is ${Number(result)}`);

// if (result>200){
//     alert("greater than 200");
// }
// else if (result == 200) {
//     alert("equals 200");
// }
// else {
//     alert("smaller than 200");
// }

// result = (result > 200);
// if (result) {
//     alert(+fruits + +veggies);
// }
// else {
//     alert(+fruits * +veggies);
// }

let numbah = prompt("gimme tha numbah", 1);
let tellya = (numbah < 0) ? 'negative' : (numbah == 0) ? 'zerrro' : (numbah > 0) ? "positive" : "hmmm";
alert(tellya);

