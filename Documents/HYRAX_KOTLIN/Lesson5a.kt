//OOP - Object Oriented Programming - Its Coding Style
//We Create and use Objects n Code
//Advantage of Objects
//1.Code Reuse - 1 can be used severally
//2.Makes code Easy to Understand
//3.Creates way to learn More advanced concepts
//We use classes in OOP,Your code will always go in a class
//A class holds the object
class Arithmetic{
    //States and behaviour
    //States - Properties/Fields/Data Members
    //Behaviour - Function
    // Data Members
    private val  num1: Int = 50
    private val num2:Int =89

    //Member functions
    public fun findSum (){
         val answer = num1 + num2
         println("Sum is $answer")
    }//end

    public fun findProduct(){
        val answer = num1 *num2
        println("The multiplication is $answer")
    }
    
    public fun findDivision(){
        val answer = num2 / num1
        println("The division is $answer")
    }

    public fun findSubtract(){
        val answer = num2 - num1
        println("The subtraction is $answer")
    }


}//end


//Create the main
fun main(){
    //Access your object
    val myObject = Arithmetic()

    //Access data member and function
    myObject.findSum()
    myObject.findProduct()
     
    // Access data member and functions

    myObject.findDivision()
    myObject.findSubtract()


}
