fun main(){
    //Control statements
    //IF,IF ELSE,ELSE IF,WHEN,WHILE,FOR
    ///1.IF statement
     val marks:Short = 30
     if(marks > 0 && marks < 30 ){
        println("You scored $marks ,Its a Fail")
     }
     

     else if (marks in 30 ..50){
        println("You scored $marks ,Its Average")
     }


     else if (marks in 51 .. 70){
        println("You scored $marks,Its above Average")
     }


     else if (marks  in 71.. 100 ){
        println("You scored $marks , Excellent")
     }


     else{
        println("Not Allowed")
     }

}//end main
//ELSE does not have a condition